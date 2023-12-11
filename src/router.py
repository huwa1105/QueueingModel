import queue

from simulator import Simulator


class Router:
    def __init__(self, queue_size):
        self.queue = queue.Queue(queue_size)
        self.dropped_packets = 0

    def enqueue_packet(self, packet):
        try:
            packet.position_in_queue_R_arrival = self.queue.qsize()
            self.queue.put_nowait(packet)
            packet.timestamp_B_arrival = Simulator.now()
        except queue.Full:
            packet.dropped = True
            self.dropped_packets += 1

    def dequeue_packet(self, simulator):
        if not self.queue.empty():
            return self.queue.get()
        return None
