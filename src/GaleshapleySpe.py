from src.Agent import Agent
from src.AgentsExtracteur import AgentExtracteur
from src.Galeshapley import Galeshapley
from src.Postulant import Postulant


class GaleshapleySpe(Galeshapley):
    def __init__(self):
        super().__init__(AgentExtracteur('PrefSpe.txt', Agent).agents, AgentExtracteur('PrefEtu.txt', Postulant).agents)

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
