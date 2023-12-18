import time
import threading
import logging

from router import Router
from link import Link
from host import Host
from packet import Packet


def main():
    # Util_variables
    event_list = []

    # Create hosts
    hostA = Host()
    hostB = Host()

    # Create router
    router = Router()
    router.queue_size_in_octets = 500

    # Create links
    linkAR = Link()
    linkAR.distance = 1000
    linkAR.debit = 500000

    linkRB = Link()
    linkRB.distance = 1000
    linkRB.debit = 1000000

    # Packets generation
    def generate_packet():
        i = 0
        while True:
            i += 1
            time.sleep(1)
            packet = Packet(i, 1000, 0, False, None, None, None, None)
            event_list.append(packet)
            logging.info(f"Packet {i} generated")

    t_packet = threading.Thread(target=generate_packet, name="packet_generation")

    for i in range(0, 10):
        packet = Packet(order=i, size=1000, dropped=False)
        event_list.append(packet)

    # Send packets

    def send_packet():
        while True:
            if len(event_list) > 0:
                packet = event_list.pop(0)
                sent_packet = hostA.send(packet, linkAR, router)
                print(f"Packet {sent_packet} sent from HostA to Router")




    t_send = threading.Thread(target=send_packet, name="packet_sending")

    #t_packet.start()
    t_send.start()


if __name__ == "__main__":
    main()
