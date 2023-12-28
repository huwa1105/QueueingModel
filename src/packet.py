from dataclasses import dataclass
from datetime import datetime
@dataclass
class Packet:
    order: int  # define the order of the packet
    size: int  # define the size of the packet in bits
    dropped: bool  # if the packet has been dropped from the router
    positionInQueue: int | None = None  # the position in the queue of the router
    startDepartureTimeFromHost: datetime | None = None  # the time of departure from the hostA
    endDepartureTimeFromHost: datetime | None = None  # the time of departure from the hostA
    startArrivalTimeToRouter: datetime | None = None  # the time of arrival at the router
    endArrivalTimeToRouter: datetime | None = None  # the time of arrival at the router
    startDepartureTimeFromRouter: datetime | None = None  # the time of departure from the router
    endDepartureTimeFromRouter: datetime | None = None  # the time of departure from the router
    startArrivalTimeToDestination: datetime | None = None  # the time of arrival at the hostB
    endArrivalTimeToDestination: datetime | None = None  # the time of arrival at the hostB
