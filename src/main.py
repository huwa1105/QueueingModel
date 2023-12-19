import time
import threading
import logging
from pprint import pprint

from router import Router
from link import Link
from host import Host
from packet import Packet

# TODO Assure sync for shared list between threads
# TODO Find a way to display result


def main():
    # Util_variables
    event_list = []
    all_packets_result = []

    sent_packets_linkAR = []
    sent_packets_linkRB = []

    # Create hosts
    hostA = Host()
    hostB = Host()

    # Create router
    router = Router()
    router.queue_size_in_octets = 1000

    # Create links
    linkAR = Link()
    linkAR.distance = 200
    linkAR.debit = 5000

    linkRB = Link()
    linkRB.distance = 200
    linkRB.debit = 1000

    # Packets generation
    def generate_packet():
        i = 0
        while True:
            i += 1
            packet = Packet(i, 1000, 0, False, None, None, None, None)
            event_list.append(packet)
            # print(f"Packet {i} generated")

    t_packet = threading.Thread(target=generate_packet, name="packet_generation")

    for i in range(0, 1000):
        packet = Packet(order=i, size=1000, dropped=False)
        event_list.append(packet)

    # Send packets
    def host_send_packet():
        while True:
            if len(event_list) > 0:
                sent_packet = event_list.pop(0)
                sent_packet = hostA.send(sent_packet, linkAR)
                # print(f"\nPacket {sent_packet} sent by host")
                sent_packets_linkAR.append(sent_packet)

    def router_recv_packet():
        while True:
            if len(sent_packets_linkAR) > 0:
                received_packet = sent_packets_linkAR.pop(0)
                dropped_packet = router.recv(received_packet, linkAR)
                if dropped_packet:
                    all_packets_result.append(dropped_packet)
                # print(f"\nPacket {received_packet} received by router")

    def router_send_packet():
        while True:
            if len(router.queue) > 0:
                sent_packet = router.queue.pop(0)
                sent_packet = router.send(sent_packet, linkRB)
                # print(f"\nPacket {sent_packet} sent by router")
                sent_packets_linkRB.append(sent_packet)

    def host_recv_packet():
        while True:
            if len(sent_packets_linkRB) > 0:
                received_packet = sent_packets_linkRB.pop(0)
                hostB.recv(received_packet, linkRB)
                all_packets_result.append(received_packet)
                print(f"\nPacket {received_packet} received by hostB")

    t_host_send = threading.Thread(target=host_send_packet, name="host_packet_sending")
    t_router_recv = threading.Thread(target=router_recv_packet, name="router_packet_receiving")
    t_router_send = threading.Thread(target=router_send_packet, name="router_packet_sending")
    t_host_recv = threading.Thread(target=host_recv_packet, name="host_packet_receiving")

    # t_packet.start()
    t_host_send.start()
    t_router_recv.start()
    t_router_send.start()
    t_host_recv.start()


if __name__ == "__main__":
    main()
