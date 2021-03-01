from src.Reader import Reader


class AgentExtracteur:
    def __init__(self, nomFichier, constructeur):
        self.reader = Reader()
        self.agents = self.extraireAgents(nomFichier, constructeur)

    def extraireAgents(self, nomFichier, constructeur):
        rawAgents = self.formatterListe(self.reader.execute(nomFichier))
        rawAgents.pop(0)
        def extraireLigne(ligne):
            capacite = ligne[0]
            id = ligne[1]
            nom = ligne[2]
            souhaits = list(map(lambda souhait: int(souhait), ligne[3:]))
            return constructeur(id, nom, souhaits, capacite)
        if rawAgents[0][0] == 'Cap':
            capacites = rawAgents.pop(0)
            capacites.pop(0)
            capacites = list(map(lambda capacite: int(capacite), capacites))
        else:
            capacites = [1] * len(rawAgents)
        for index, agent in enumerate(rawAgents):
            agent.insert(0, capacites[index])
        return list(map(extraireLigne, rawAgents))


    def formatterListe(self, liste):
        return list(map(
            lambda ligne: ligne \
                if type(ligne) is list \
                else ligne.strip('\n').split('\t'),
            liste))