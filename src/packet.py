class Packet:
    def __init__(self, size):
        self.size = size
        self.timestamp_A_depart = None
        self.timestamp_R_arrival = None
        self.position_in_queue_R_arrival = None
        self.timestamp_B_arrival = None
        self.dropped = False

    def __repr__(self):
        return (
            f"Packet(size={self.size}, "
            f"timestamp_A_depart={self.timestamp_A_depart}, "
            f"timestamp_R_arrival={self.timestamp_R_arrival}, "
            f"position_in_queue_R_arrival={self.position_in_queue_R_arrival}, "
            f"timestamp_B_arrival={self.timestamp_B_arrival}, "
            f"dropped={self.dropped})"
        )
