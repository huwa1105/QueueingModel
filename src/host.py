import datetime
import logging
import threading
import time

from router import Router


class Host:

    def send(self, packet, link):  # send the data

        packet.startDepartureTimeFromHost = datetime.datetime.now()

        link.transmission(packet)

        packet.endDepartureTimeFromHost = datetime.datetime.now()

        return packet


    def recv(self, packet, link):  # receive the data
        packet.startArrivalTimeToDestination = datetime.datetime.now()
        packet.endArrivalTimeToDestination = datetime.datetime.now()
        return packet
