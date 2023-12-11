import datetime
import threading
import time


class Host:
    def send(self, data, link):  # send the data
        data.startdeparureTimeFromHost = datetime.datetime.now()
        transmission_time = data.size / link.debit
        print(f"Transmission time: {transmission_time}")
        data.enddeparureTimeFromHost = data.startdeparureTimeFromHost + datetime.timedelta(seconds=transmission_time)
        print(f"Packet start departure time from host: {data.startdeparureTimeFromHost} and end at {data.enddeparureTimeFromHost}")


    def recv(self):  # receive the data
        return "data"
