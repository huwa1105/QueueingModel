import datetime
import threading
import time


class Router:
    queue_size_in_octets: int = 0  # the queue is in octets
    queue = []
    dropped_packets = []
    previous_packet = None
    sum_of_packets_size_in_queue = 0

    def recv(self, packet, link):
        while True:

            queue_size = self.queue_size_in_octets * 8  # the queue is in bits

            packet.startArrivalTimeToRouter = packet.startDepartureTimeFromHost + datetime.timedelta(
                seconds=link.propagation())
            packet.endArrivalTimeToRouter = packet.endDepartureTimeFromHost + datetime.timedelta(
                seconds=link.propagation())

            packet.position_in_queue = len(self.queue) + 1

            if (packet.size + self.sum_of_packets_size_in_queue) <= queue_size:
                packet.dropped = False
                self.queue.append(packet)
                self.sum_of_packets_size_in_queue += packet.size
            else:
                packet.dropped = True
                self.dropped_packets.append(packet)

            return packet

    def send(self, packet, link):
        while True:
            if len(self.queue) > 0:
                time.sleep(
                    self.previous_packet.endDepartureTimeFromRouter - self.previous_packet.startDepartureTimeFromRouter)

                current_packet = self.queue.pop(0)
                current_packet.startDepartureTimeFromRouter = self.previous_packet.endDepartureTimeFromRouter
                current_packet.endDepartureTimeFromRouter = packet.startDepartureTimeFromRouter + datetime.timedelta(
                    seconds=packet.size / link.debit)

                current_packet.startArrivalTimeToDestination = current_packet.startDepartureTimeFromRouter + datetime.timedelta(
                    seconds=link.propagation())
                current_packet.endArrivalTimeToDestination = current_packet.endDepartureTimeFromRouter + datetime.timedelta(
                    seconds=link.propagation())

                self.previous_packet = current_packet

                for packets in self.queue:
                    packets.position_in_queue -= 1

            return packet

    t_recv = threading.Thread(target=recv, name="packet_receiving")
    # t_send = threading.Thread(target=send, name="packet_sending")

    # t_send.start()
