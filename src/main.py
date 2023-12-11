from src.host import Host
from src.link import Link
from src.packet import Packet
from src.router import Router
from src.simulator import Simulator


def main():
    # Exemple d'utilisation
    link1 = Link(distance=100, propagation_speed=200000000, transmission_speed=1000000)
    link2 = Link(distance=100, propagation_speed=200000000, transmission_speed=1000000)
    router = Router(queue_size=10)
    hostA = Host()
    hostB = Host()

    # Simulation
    packets = []
    simulator = Simulator()

    for i in range(20):
        packet = Packet(size=100)
        hostA.send_packet(packet, link1, simulator)
        packets.append(packet)

    while True:
        packet = router.dequeue_packet(simulator)
        if packet is not None:
            hostB.receive_packet(packet, router, simulator)
        else:
            break

    # Affichage des résultats
    for i, packet in enumerate(packets):
        print(f"Paquet {i + 1}: {packet}")


if __name__ == "__main__":
    main()
