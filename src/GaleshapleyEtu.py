from src.Agent import Agent
from src.AgentsExtracteur import AgentExtracteur
from src.Galeshapley import Galeshapley
from src.Postulant import Postulant


class GaleshapleyEtu(Galeshapley):
    def __init__(self, postulants, postules):
        super().__init__(postulants, postules)
