from time import time

from src.Agent import Agent
from src.AgentsExtracteur import AgentExtracteur
from src.CurveDrawer import CurveDrawer
from src.GaleshapleyEtu import GaleshapleyEtu
from src.GaleshapleyEtuFromFile import GaleshapleyEtuFromFile
from src.GaleshapleyEtuRandom import GaleshapleyEtuRandom
from src.Postulant import Postulant

galeShapleyEtuFromFile = GaleshapleyEtuFromFile()

postules = galeShapleyEtuFromFile.postules
"""for postule in postules:
    print(postule.toString())"""
print()
galeShapleyEtuFromFile.execute()
print(galeShapleyEtuFromFile.postulantsToString())
print(galeShapleyEtuFromFile.postulesToString())
print()
print()
print()
print()
durees = dict()
for i in range(200, 20001, 200):
    galeShapleyEtuRandom = GaleshapleyEtuRandom(i, 'Etu', AgentExtracteur('PrefSpe.txt', Agent).agents)
    start = time()
    galeShapleyEtuRandom.execute()
    end = time()
    print(galeShapleyEtuRandom.postulantsToString())
    print(galeShapleyEtuRandom.postulesToString())
    totalMs = (end - start) * 1000
    durees[i] = totalMs
for nbEtu in durees.keys():
    print("""nombre d'étudiants: {}
          temps total: {} millisecondes""".format(nbEtu, durees[nbEtu]))
print(durees.keys())
print(durees.values())
drawer = CurveDrawer(durees.keys(), durees.values())
drawer.draw()
