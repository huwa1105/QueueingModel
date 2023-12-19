import os
import time
import threading
import logging
import toml

from router import Router
from link import Link
from host import Host
from packet import Packet


# TODO Assure sync for shared list between threads


def main():

    config_file = "case1.toml"

    with open(config_file, "r") as f:
        config = toml.load(f)

    # Util_variables
    event_list = []
    all_packets_result = []
    rate: int = int(config['parameter']['rate'])  # packets per second
    global flag
    flag = False

    sent_packets_linkAR = []
    sent_packets_linkRB = []

    # Create hosts
    hostA = Host()
    hostB = Host()

    # Create router
    router = Router()
    router.queue_size_in_octets = int(config['parameter']['queue_size'])

    # Create links
    linkAR = Link()
    linkAR.distance = int(config['parameter']['distance_link_1'])
    linkAR.debit = int(config['parameter']['debit_link_1'])
    linkAR.speed = int(config['parameter']['speed'])

    linkRB = Link()
    linkRB.distance = int(config['parameter']['distance_link_2'])
    linkRB.debit = int(config['parameter']['debit_link_2'])
    linkRB.speed = int(config['parameter']['speed'])

    # Packets generation
    def generate_packet():
        global flag
        for i in range(0, int(config['parameter']['number_of_packets'])):
            packet = Packet(order=i, size=1000, dropped=False)
            event_list.append(packet)
            time.sleep(1 / rate)

        #print("\nAll packets have been generated\n")
        flag = True

    t_packet = threading.Thread(target=generate_packet, name="packet_generation")

    # Send packets
    def host_send_packet():
        cmpt =0
        while cmpt < int(config['parameter']['number_of_packets']):
            if event_list:
                cmpt += 1
                sent_packet = event_list.pop(0)
                sent_packet = hostA.send(sent_packet, linkAR)
                # print(f"\nPacket {sent_packet} sent by host")
                sent_packets_linkAR.append(sent_packet)
        print(f"\nAll packets have been sent by host {cmpt}")

    def router_recv_packet():
        cmpt = 0
        while cmpt < int(config['parameter']['number_of_packets']):
            if sent_packets_linkAR:
                cmpt += 1
                received_packet = sent_packets_linkAR.pop(0)
                dropped_packet = router.recv(received_packet, linkAR)
                if dropped_packet:
                    all_packets_result.append(dropped_packet)
                # print(f"\nPacket {received_packet} received by router")
        print(f"\nAll packets have been received by router {cmpt}")


    def router_send_packet():
        cmpt = 0
        while cmpt < int(config['parameter']['number_of_packets']) - router.dropped_count:
            if router.queue:
                cmpt += 1
                sent_packet = router.queue.pop(0)
                sent_packet = router.send(sent_packet, linkRB)
                # print(f"\nPacket {sent_packet} sent by router")
                sent_packets_linkRB.append(sent_packet)
        print(f"\nAll packets have been sent by router {cmpt}")


    def host_recv_packet():
        cmpt = 0
        while cmpt < int(config['parameter']['number_of_packets']) - router.dropped_count:
            if sent_packets_linkRB:
                cmpt += 1
                received_packet = sent_packets_linkRB.pop(0)
                hostB.recv(received_packet, linkRB)
                all_packets_result.append(received_packet)
                print(f"\nPacket {received_packet} received by host")
        print(f"\nAll packets have been received by host {cmpt}\n")
        all_packets_result.sort(key=lambda x: x.order)
        for element in all_packets_result:
            print(f"{element.order}\t{element.startDepartureTimeFromHost}\t{element.endArrivalTimeToRouter}\t{element.startDepartureTimeFromRouter}\t{element.endArrivalTimeToDestination}\t{element.positionInQueue}\t{element.dropped}")

    t_host_send = threading.Thread(target=host_send_packet, name="host_packet_sending")
    t_router_recv = threading.Thread(target=router_recv_packet, name="router_packet_receiving")
    t_router_send = threading.Thread(target=router_send_packet, name="router_packet_sending")
    t_host_recv = threading.Thread(target=host_recv_packet, name="host_packet_receiving")

    t_packet.start()
    t_host_send.start()
    t_router_recv.start()
    t_router_send.start()
    t_host_recv.start()

    t_packet.join()
    t_host_send.join()
    t_router_recv.join()
    t_router_send.join()
    t_host_recv.join()


if __name__ == "__main__":
    main()
