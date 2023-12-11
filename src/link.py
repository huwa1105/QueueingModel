"""Here are the formulas that we apply to the links.
speed of propagation : s = d/tp where d = the distance traveled in meters and
tp = the time taken to cover this distance in meters per second
time of transmission : t = L/R where L = the packet size in Bits and
 R = the transmission rate in Bits per second
"""

class Link:
    distance: int  # in meters
    speed: int = 200000  # m/s, 2/3 of speed of light
    debit: int   # the debit is in bits/s
