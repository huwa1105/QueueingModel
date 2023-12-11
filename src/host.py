class Host:
    def send_packet(self, packet, link, simulator):
        packet.timestamp_A_depart = simulator.now()
        link.transmit(packet, simulator)

    def receive_packet(self, packet, router, simulator):
        router.enqueue_packet(packet)
