import random
from math import ceil


class Agent:
    def __init__(self, id, nom, souhaits, capacite=1):
        self.id = int(id)
        self.nom = nom
        self.estLibre = True
        self.capacite = capacite
        self.affectations = []
        self.souhaits = list(map(lambda souhait: int(souhait), souhaits))
        self.candidatures = []

    def libererPlace(self):
        postulant = self.affectations.pop()
        postulant.liberer()

    def dernierPostulantAffecte(self):
        return self.affectations[len(self.affectations) - 1]

    def affecter(self, agent):
        if not self.capaciteMaxAtteinte():
            self.affectations.append(agent)
            self.ajouterCandidature(agent)
            agent.ajouterCandidature(self)
        else:
            print("Erreur, capacite max atteinte")

    def ajouterCandidature(self, agent):
        self.candidatures.append(agent)

    def compare(self, agent1, agent2):
        return self.souhaits.index(agent1.id) < self.souhaits.index(agent2.id)

    def capaciteMaxAtteinte(self):
        return len(self.affectations) >= self.capacite

    def toString(self):
        return "id: {}, nom: {}, capacite: {}, souhaits: {}".format(self.id, self.nom, self.capacite, self.souhaits) + " agents affectes: {}".format(
            list(map(lambda agent: agent.nom, self.affectations)))

    @staticmethod
    def genererPrefAgents(preferants, preferes):
        for preferant in preferants:
            for i in preferes:
                notExists = True
                souhait = -1
                while notExists:
                    notExists = True
                    souhait = random.randint(0, len(preferes) - 1)
                    if souhait not in preferant.souhaits:
                        notExists = False
                preferant.souhaits.append(souhait)
                preferant.capacite = 1
        capaciteAjoutable = len(preferes) - len(preferants)
        if capaciteAjoutable > 0:
            i = 0
            while not capaciteAjoutable == 0:
                capaciteAjoutee = random.randint(0, int(ceil(capaciteAjoutable / len(preferants))))
                preferants[i % len(preferants)].capacite += capaciteAjoutee
                capaciteAjoutable = capaciteAjoutable - capaciteAjoutee
                i = i + 1
        return preferants
