import datetime
from threading import Lock


class Router:
    queue_size_in_octets: int = 1000  # the queue is in octets
    queue = []
    sum_of_packets_size_in_queue = 0
    dropped_count = 0
    queue_size = queue_size_in_octets * 8  # the queue is in bits


    def recv(self, packet, link):
        packet.startArrivalTimeToRouter = datetime.datetime.now()
        propagation_time = link.propagation()
        packet.endArrivalTimeToRouter = packet.endDepartureTimeFromHost + datetime.timedelta(seconds=propagation_time)
        packet.positionInQueue = len(self.queue) + 1

        if (packet.size + self.sum_of_packets_size_in_queue) <= self.queue_size:
            packet.dropped = False
            self.queue.append(packet)
            self.sum_of_packets_size_in_queue += packet.size
        else:
            packet.dropped = True
            self.dropped_count += 1
            return packet

    def send(self, packet, link):
        packet.startDepartureTimeFromRouter = datetime.datetime.now()
        link.transmission(packet)
        packet.endDepartureTimeFromRouter = datetime.datetime.now()
        self.sum_of_packets_size_in_queue -= packet.size
        return packet
