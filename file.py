class Writer:
    def __init__(self, nom, contenu, extension='txt'):
        self.nom = nom
        self.contenu = contenu
        self.extension = extension

    def setFichier(self, nom, contenu, extension='txt'):
        self.nom = nom
        self.contenu = contenu
        self.extension = extension

    def execute(self):
        fichier = open(self.nom + '.' + self.extension, 'w')
        fichier.write(self.contenu)
        fichier.close()