"""Here are the formulas that we apply to the links.
speed of propagation : s = d/tp where d = the distance traveled in meters and
tp = the time taken to cover this distance in meters per second
time of transmission : t = L/R where L = the packet size in Bits and
 R = the transmission rate in Bits per second
"""
import time


class Link:
    distance: int  # in meters
    speed: int = 100  # m/s, 2/3 of speed of light
    debit: int   # the debit is in bits/s

    def propagation(self):
        propagation_time = self.distance / self.speed
        #print(f"Propagation time: {propagation_time}")
        time.sleep(propagation_time)
        return propagation_time

    def transmission(self, packet):
        transmission_time = packet.size / self.debit
        #print(f"Transmission time: {transmission_time}")
        time.sleep(transmission_time)
        return transmission_time
