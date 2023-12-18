import datetime
import threading
import time


class Router:
    queue_size_in_octets: int = 1000  # the queue is in octets
    queue = []
    dropped_packets = []
    sum_of_packets_size_in_queue = 0
    dropped_count = 0

    def recv(self, packet, link):

        queue_size = self.queue_size_in_octets * 8  # the queue is in bits
        propagation_time = link.propagation()

        packet.startArrivalTimeToRouter = packet.startDepartureTimeFromHost + datetime.timedelta(
            seconds=propagation_time)
        packet.endArrivalTimeToRouter = packet.endDepartureTimeFromHost + datetime.timedelta(
            seconds=propagation_time)

        packet.positionInQueue = len(self.queue) + 1

        if (packet.size + self.sum_of_packets_size_in_queue) <= queue_size:
            packet.dropped = False
            self.queue.append(packet)
            self.sum_of_packets_size_in_queue += packet.size
        else:
            packet.dropped = True
            self.dropped_packets.append(packet)
            self.dropped_count += 1

        return self.queue

    def send(self, packet, link):
        if len(self.queue) > 0:

            packet.startDepartureTimeFromRouter = datetime.datetime.now()

            link.transmission(packet)
            packet.endDepartureTimeFromRouter = datetime.datetime.now()

            self.sum_of_packets_size_in_queue -= packet.size

            return packet
