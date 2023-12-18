import datetime
import logging
import threading
import time

from router import Router


class Host:

    previous_packet = None

    def send(self, packet, link, router):  # send the data

        transmission_time = packet.size / link.debit

        if self.previous_packet is None:
            packet.startDepartureTimeFromHost = datetime.datetime.now()

        else:
            packet.startDepartureTimeFromHost = self.previous_packet.endDepartureTimeFromHost

        packet.endDepartureTimeFromHost = packet.startDepartureTimeFromHost + datetime.timedelta(seconds=transmission_time)

        self.previous_packet = packet

        packet = router.recv(packet, link)

        return packet


    def recv(self):  # receive the data
        return "data"
