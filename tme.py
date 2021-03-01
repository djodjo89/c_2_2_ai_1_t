import exemple

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
            etudiantCourant.affecter(speCourante)
        else:
            dernierEtudiantAffecte = speCourante.dernierPostulantAffecte()
            if speCourante.compare(etudiantCourant, dernierEtudiantAffecte):
                speCourante.libererPlace()
                speCourante.affecter(etudiantCourant)
            etudiantCourant.affecter(speCourante)
            else:
                speCourante.ajouterCandidature(etudiantCourant)
    return (etudiants, specialites)