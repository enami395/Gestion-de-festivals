import sqlite3

class Artiste:
    def __init__(self, nom, type_artiste, info_supplementaire):
        self.nom = nom
        self.type_artiste = type_artiste
        self.info_supplementaire = info_supplementaire

    def ajouter_artiste(self):
        db = sqlite3.connect('festival.db')
        db.execute("insert into artistes(nom, type, info_supplementaire) values(?, ?, ?)", (self.nom, self.type_artiste, self.info_supplementaire))
        db.commit()
        db.close()

    def get_nom(self):
        return self.nom

class Musicien(Artiste):
    def __init__(self, nom, instrument):
        Artiste.__init__(self, nom, "Musicien", instrument)

class DJ(Artiste):
    def __init__(self, nom, style_musical):
        Artiste.__init__(self, nom, "DJ", style_musical)