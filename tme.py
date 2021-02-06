import exemple


class Agent:
    def __init__(self, id, nom, souhaits):
        self.id = int(id)
        self.nom = nom
        self.estLibre = True
        self.souhaits = list(map(lambda souhait: int(souhait), souhaits))
        self.candidatures = []

    def ajouterCandidature(self, agent):
        self.candidatures.append(agent)
        agent.candidatures.append(self)

    def compare(self, agent1, agent2):
        return self.souhaits.index(agent1.id) < self.souhaits.index(agent2.id)

    def toString(self):
        return "id: {}, nom: {}, souhaits: {}".format(self.id, self.nom, self.souhaits)

class Etudiant(Agent):
    def __init__(self, id, nom, souhaits):
        super().__init__(id, nom, souhaits)
        self.speCourante = None

    def affecter(self, specialite):
        self.estLibre = False
        self.speCourante = specialite

    def liberer(self):
        self.estLibre = True
        self.speCourante = None

    def aCandidateA(self, specialite):
        return self in specialite.candidatures

    def toString(self):
        return super().toString() + " specialite courante: {}".format('aucune' if self.speCourante == None else self.speCourante.nom)


class Specialite(Agent):
    def __init__(self, id, nom, souhaits, capacite):
        super().__init__(id, nom, souhaits)
        self.capacite = capacite
        self.etudiantsAffectes = []

    def capaciteMaxAtteinte(self):
        return len(self.etudiantsAffectes) >= self.capacite

    def affecter(self, etudiant):
        if not self.capaciteMaxAtteinte():
            self.etudiantsAffectes.append(etudiant)
            self.ajouterCandidature(etudiant)
            etudiant.affecter(self)
        else:
            print("Erreur, capacite max atteinte")

    def libererPlace(self):
        etudiant = self.etudiantsAffectes.pop()
        etudiant.liberer()

    def dernierEtudiantAffecte(self):
        return self.etudiantsAffectes[len(self.etudiantsAffectes) - 1]

    def toString(self):
        return super().toString() + " etudiants affectes: {}".format(list(map(lambda etudiant: etudiant.nom, self.etudiantsAffectes)))

def formatterListe(liste):
    return list(map(
        lambda ligne: ligne \
            if type(ligne) is list \
            else ligne.strip('\n').split('\t'),
        liste))


def lireFichierEtu():
    return formatterListe(exemple.lectureFichier("PrefEtu.txt"))


def lireFichierSpe():
    return formatterListe(exemple.lectureFichier("PrefSpe.txt"))


def etudiantsLibres(etudiants):
    return list(filter(
        lambda etudiant: etudiant.estLibre,
        etudiants))


def auMoinsUnEtudiantLibre(etudiants):
    return len(etudiantsLibres(etudiants)) >= 1


def auMoinsUnEtudiantLibreQuiNAPasProposeAToutLeMonde(etudiants, specialites):
    aProposeAToutLeMonde = lambda etudiant: len(etudiant.candidatures) == len(specialites)
    return auMoinsUnEtudiantLibre(etudiants) \
    and not len(list(filter(aProposeAToutLeMonde, etudiants))) == len(etudiants)


def premiereSpeSansProposition(etudiant, specialites):
    return specialites[list(filter(
        lambda souhait: not etudiant.aCandidateA(specialites[souhait]),
        etudiant.souhaits))[0]]


def extractLigneEtudiant(ligneEtudiant):
    id = ligneEtudiant[0]
    nom = ligneEtudiant[1]
    souhaits = list(map(lambda souhait: int(souhait), ligneEtudiant[2:]))
    return Etudiant(id, nom, souhaits)


def extractLigneSpecialte(ligneSpecialite):
    capacite = ligneSpecialite[0]
    id = ligneSpecialite[1]
    nom = ligneSpecialite[2]
    souhaits = ligneSpecialite[3:]
    return Specialite(id, nom, souhaits, capacite)


def galeShapley(etudiants, specialites):
    etudiants.pop(0)
    specialites.pop(0)
    capacites = specialites.pop(0)
    capacites.pop(0)
    capacites = list(map(lambda capacite: int(capacite), capacites))
    for index, specialite in enumerate(specialites):
        specialite.insert(0, capacites[index])
    etudiants = list(map(extractLigneEtudiant, etudiants))
    specialites = list(map(extractLigneSpecialte, specialites))
    while auMoinsUnEtudiantLibreQuiNAPasProposeAToutLeMonde(etudiants, specialites):
        etudiantCourant = etudiantsLibres(etudiants)[0]
        speCourante = premiereSpeSansProposition(etudiantCourant, specialites)
        if not speCourante.capaciteMaxAtteinte():
            speCourante.affecter(etudiantCourant)
        else:
            dernierEtudiantAffecte = speCourante.dernierEtudiantAffecte()
            if speCourante.compare(etudiantCourant, dernierEtudiantAffecte):
                speCourante.libererPlace()
                speCourante.affecter(etudiantCourant)
            else:
                speCourante.ajouterCandidature(etudiantCourant)
    return (etudiants, specialites)