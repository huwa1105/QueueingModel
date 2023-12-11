import router
import simulator
from router import Router
from simulator import Event, Simulator


class Link:
    def __init__(self, distance, propagation_speed, transmission_speed):
        self.distance = distance
        self.propagation_speed = propagation_speed
        self.transmission_speed = transmission_speed

    def transmit(self, packet, simulator):
        transmission_time = packet.size / self.transmission_speed
        propagation_time = self.distance / self.propagation_speed
        total_time = transmission_time + propagation_time
        simulator.add_event(Event(packet, self._transmit_callback), total_time)

    def _transmit_callback(self, packet):
        packet.timestamp_R_arrival = simulator.now()
        router.enqueue_packet(packet)