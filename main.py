from exemple import createFichierLP
from file import Writer
from tme import lireFichierEtu, lireFichierSpe, galeShapley

(etudiants, specialites) = galeShapley(lireFichierEtu(), lireFichierSpe())
contenuFichierEtudiants = ''
contenuFichierSpecialites = ''
for etudiant in etudiants:
    contenuFichierEtudiants += etudiant.toString() + '\n'
for specialite in specialites:
    contenuFichierSpecialites += specialite.toString() + '\n'

ecrivain = Writer('affectationsEtudiants', contenuFichierEtudiants)
ecrivain.execute()
ecrivain.setFichier('affectationsSpecialites', contenuFichierSpecialites)
ecrivain.execute()