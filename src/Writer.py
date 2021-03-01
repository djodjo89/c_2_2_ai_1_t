class Writer:
    def __init__(self, extension='txt'):
        self.extension = extension

    def setExtension(self, extension='txt'):
        self.extension = extension

    def execute(self, nom, contenu):
        fichier = open(nom + '.' + self.extension, 'w')
        fichier.write(contenu)
        fichier.close()