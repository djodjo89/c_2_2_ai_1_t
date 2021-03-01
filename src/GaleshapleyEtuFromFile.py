from src.Agent import Agent
from src.AgentsExtracteur import AgentExtracteur
from src.GaleshapleyEtu import GaleshapleyEtu
from src.Postulant import Postulant


class GaleshapleyEtuFromFile(GaleshapleyEtu):
    def __init__(self):
        super().__init__(AgentExtracteur('PrefEtu.txt', Postulant).agents, AgentExtracteur('PrefSpe.txt', Agent).agents)
