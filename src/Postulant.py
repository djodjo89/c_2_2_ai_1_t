from src.Agent import Agent


class Postulant(Agent):
    def __init__(self, id, nom, souhaits, capacite):
        super().__init__(id, nom, souhaits, capacite)
        self.postuleCourant = None

    def affecter(self, postule):
        super().affecter(postule)
        if self.capaciteMaxAtteinte():
            self.estLibre = False
        self.postuleCourant = postule

    def liberer(self):
        self.estLibre = True
        self.postuleCourant = None

    def aCandidateA(self, postule):
        return self in postule.candidatures

    def toString(self):
        return super().toString() + " postule courant: {}".format('aucun' if self.postuleCourant == None else self.postuleCourant.nom)

    @staticmethod
    def genererPostulants(nb, nomDeBase ='Postulant'):
        postulants = []
        for i in range(nb):
            postulants.append(Postulant(i, nomDeBase + str(i), [], 1))
        return postulants