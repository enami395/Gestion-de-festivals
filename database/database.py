import sqlite3

def creer_base_donnees():
    db = sqlite3.connect('festival.db')
    db.execute("create table if not exists artistes(nom text, type text, info_supplementaire text)")
    db.execute("create table if not exists festivals(nom text, date text, artistes text)")
    db.commit()
    db.close()