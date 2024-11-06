import sqlite3

class Festival:
    def __init__(self, nom, date):
        self.nom = nom
        self.date = date
        self.artistes = []

    def ajouter_artiste(self, artiste):
        self.artistes.append(artiste)

    def ajouter_festival(self):
        db = sqlite3.connect('festival.db')

        for artiste in self.artistes:
            db.execute("insert into festivals(nom, date, artistes) values(?, ?, ?)", (self.nom, self.date, artiste.get_nom()))
        db.commit()
        db.close()

