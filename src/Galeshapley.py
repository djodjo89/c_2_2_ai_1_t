from src.Agent import Agent
from src.AgentsExtracteur import AgentExtracteur
from src.Reader import *
from src.Postulant import Postulant
from src.Writer import Writer


class Galeshapley:
    def __init__(self, postulants, postules):
        self.postulants = postulants
        self.postules = postules
        for i in self.postules:
            i.souhaits = []
        for i in self.postulants:
            i.souhaits = []
        Agent.genererPrefAgents(self.postulants, self.postules)
        Agent.genererPrefAgents(self.postules, self.postulants)
        self.ecrivain = Writer()

    def premierPostuleSansProposition(self, postulant):
        return self.postules[list(filter(
            lambda souhait: not postulant.aCandidateA(self.postules[souhait]),
            postulant.souhaits))[0]]

    def auMoinsUnPostulantLibreQuiNAPasProposeAToutLeMonde(self):
        aProposeAToutLeMonde = lambda postulant: len(postulant.candidatures) == len(self.postules)
        return self.auMoinsUnPostulantLibre() \
               and not len(list(filter(aProposeAToutLeMonde, self.postulants))) == len(self.postulants)

    def auMoinsUnPostulantLibre(self):
        return len(self.postulantsLibres()) >= 1

    def postulantsLibres(self):
        return list(filter(
            lambda postulant: postulant.estLibre,
            self.postulants))

    def postulantsToString(self):
        contenuFichierPostulants = ''
        for postulant in self.postulants:
            contenuFichierPostulants += postulant.toString() + '\n'
        return contenuFichierPostulants

    def postulesToString(self):
        contenuFichierPostules = ''
        for postule in self.postules:
            contenuFichierPostules += postule.toString() + '\n'
        return contenuFichierPostules

    def writePostulants(self):
        self.ecrivain.execute('affectationsPostulants', self.postulantsToString())

    def writePostules(self):
        self.ecrivain.execute('affectationsPostules', self.postulesToString())

    def affecter(self, postulant, postule):
        postulant.affecter(postule)
        postule.affecter(postulant)

    def execute(self):
        while self.auMoinsUnPostulantLibreQuiNAPasProposeAToutLeMonde():
            postulantCourant = self.postulantsLibres()[0]
            postuleCourant = self.premierPostuleSansProposition(postulantCourant)
            if not postuleCourant.capaciteMaxAtteinte():
                self.affecter(postulantCourant, postuleCourant)
            else:
                dernierPostulantAffecte = postuleCourant.dernierPostulantAffecte()
                if postuleCourant.compare(postulantCourant, dernierPostulantAffecte):
                    postuleCourant.libererPlace()
                    self.affecter(postulantCourant, postuleCourant)
                else:
                    postuleCourant.ajouterCandidature(postulantCourant)
        self.writePostulants()
        self.writePostules()








