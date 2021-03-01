from src.Agent import Agent
from src.AgentsExtracteur import AgentExtracteur
from src.GaleshapleyEtu import GaleshapleyEtu
from src.Postulant import Postulant


class GaleshapleyEtuRandom(GaleshapleyEtu):
    def __init__(self, nbPostulants, nomPostulants, postules):
        super().__init__(Postulant.genererPostulants(nbPostulants, nomPostulants), postules)
