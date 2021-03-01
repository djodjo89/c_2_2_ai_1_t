class Reader:
    def execute(self, nom):
        monFichier = open(nom, "r")
        contenu = monFichier.readlines()
        monFichier.close()
        contenu[0] = contenu[0].split()
        contenu[1] = contenu[1].split()
        return contenu