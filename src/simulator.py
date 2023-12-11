import queue
from dataclasses import dataclass, field
from typing import Any
import logging


@dataclass(order=True)
class SimulatorEvent:
    """Classe représentant un événement du simulateur comme un couple
    (temps, événement) où le temps est un flottant représentant le temps
    d'occurrence et événement est l'événement lui-même.

    Le temps est utilisé comme priorité pour la file d'événements. L'événement
    doit supporter une méthode d'instance 'run' sans argument.

    Note: implémenté comme un triplet avec le second composant étant un numéro
            unique d'événement; permet un ordre total incluant les événements
            ayant le même temps d'occurrence.
    """

    time: float
    num: int
    event: Any = field(compare=False)


class Simulator:
    _en = 0

    def __init__(self):
        self.__now = 0
        self.q = queue.PriorityQueue()
        self.__logger = logging.getLogger("simulator")

    def add_event(self, event, delta_t):
        """Ajoute un événement à la file d'attente du simulateur. L'argument
        delta_t est le délai avant l'occurrence de l'événement par rapport au
        temps courant du simulateur.
        """
        self.__logger.debug(f"{self} queueing event {event} in {delta_t} s")
        assert delta_t >= 0
        self.q.put(SimulatorEvent(self.__now + delta_t, Simulator._en, event))
        Simulator._en += 1

    def run(self):
        """Lance la simulation en exécutant tous les événements de la file
        d'attente jusqu'à ce qu'elle soit vide.
        """
        self.__logger.debug(f"running... ({self})")
        while self.q.qsize() > 0:
            self.__logger.debug(f"{self.q.qsize()} events.")
            e = self.q.get()
            self.__now = e.time
            self.__logger.debug(f"now = {self.__now}")
            e.event.run()
        self.__logger.debug("terminated.")

    def now(self):
        return self.__now

    def reset(self):
        self.__now = 0
        self.q = queue.PriorityQueue()


class Event:
    """Classe représentant un événement générique du simulateur comme un couple
    (contexte, callback). La fonction callback est appelée avec le contexte
    comme argument lors de l'occurrence de l'événement.
    """

    def __init__(self, ctx, callback):
        self.ctx = ctx
        self.callback = callback

    def run(self):
        self.callback(self.ctx)
