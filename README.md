# Queueing Model

This project is a simulation of a network with two hosts, a router, and two links. It is written in Python and uses the TOML configuration file format for setting up the parameters of the simulation.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.11
- TOML 0.10.2

### Installing

Clone the repository to your local machine:

```bash
git clone https://github.com/huwa1105/QueueingModel.git
```

Navigate to the project source directory:

```
cd QueueingModel
```

Install the required Python packages:

```
pip install -r requirements.txt
```

### Running the Simulation
To run the simulation, execute the following command:

```
python main.py -c example.toml
```

You can replace `example.toml` with the path to any other TOML configuration file.

### Configuration
The configuration file is written in the TOML format. The following is an example configuration file:

```toml
[parameter]
rate = 50 #number of packets per second (-1 = unlimited) or "[int1]_[int2]" for burst of int1 packets every int2 seconds
queue_size = 1000 #size of the queue in octets
debit_link_1 = 1000 #bits/s
distance_link_1 = 200000 #distance in meters
debit_link_2 = 500 #bits/s
distance_link_2 = 400000 #distance in meters
number_of_packets = 50 #number of packets to send
speed = 200000 #bits/s (2/3 of speed of light)
```

### Authors
- [Hugo Walem](https://moodle.umons.ac.be/user/view.php?id=57125&course=176) - [✉️ hugo.walem@student.umons.ac.be](mailto:hugo.walem@student.umons.ac.be)
- [Cyril Tongres](https://moodle.umons.ac.be/user/view.php?id=55192&course=176) - [✉️ cyril.tongres@student.umons.ac.be](mailto:cyril.tongres@student.umons.ac.be)

### License
No license
