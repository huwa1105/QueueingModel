# Packet Routing Simulation

This project simulates the process of packet routing between hosts via a router. It is implemented in Python and uses threading to simulate concurrent packet generation, sending, receiving, and routing.

## Project Structure

The project is structured into several Python files and a configuration file:

- `main.py`: This is the entry point of the application. It sets up the hosts, router, and links based on the configuration file. It also starts the threads for packet generation, sending, receiving, and routing.

- `router.py`: This file contains the `Router` class which simulates a router. The router receives packets from a host, queues them if there is enough space, and sends them to another host.

- `link.py`: This file contains the `Link` class which simulates a link between a host and a router or between a router and a host. It calculates the propagation and transmission times based on the link's distance, speed, and debit.

- `case1.toml`: This is the configuration file for the simulation. It specifies the rate of packet generation, the queue size of the router, the debit and distance of the links, the number of packets to send, and the speed of propagation.

## Running the Simulation

To run the simulation, simply execute the `main.py` file:

```bash
python main.py
```

The simulation will then start and print out the progress of packet generation, sending, receiving, and routing. At the end, it will print out the details of all packets, including their order, start and end times at the hosts and the router, their position in the queue, and whether they were dropped.

## Configuration

You can adjust the parameters of the simulation by editing the `case1.toml` file. Here is what each parameter means:  

- `rate`: The number of packets generated per second.
- `queue_size`: The size of the router's queue in octets.
- `debit_link_1` and `debit_link_2`: The debit of the links in bits/s.
- `distance_link_1` and `distance_link_2`: The distance of the links in meters.
- `number_of_packets`: The number of packets to send in the simulation.
- `speed`: The speed of propagation in bits/s (2/3 of the speed of light).

Please note that the simulation assumes that all packets have a size of 1000 octets.