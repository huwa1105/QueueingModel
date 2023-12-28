import datetime
import logging


class Host:

    def send(self, packet, link):  # send the data

        packet.startDepartureTimeFromHost = datetime.datetime.now()
        link.transmission(packet)
        packet.endDepartureTimeFromHost = datetime.datetime.now()
        return packet


    def recv(self, packet, link):  # receive the data

        propagation_time = link.propagation()
        packet.startArrivalTimeToDestination = datetime.datetime.now()
        packet.endArrivalTimeToDestination = packet.endDepartureTimeFromRouter + datetime.timedelta(seconds=propagation_time)
        return packet
