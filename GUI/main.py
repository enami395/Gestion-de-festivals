from tkinter import *
from tkinter import messagebox

from Classes.artiste import Musicien, DJ
from Classes.festival import Festival
from database.database import creer_base_donnees


def ajouter_artiste():
    nom = entry_nom.get()
    type_artiste = artiste_type.get()
    extra_info = entry_extra.get()
    nom_festival = entry_nom_festival.get()
    date_festival = entry_date_festival.get()

    if not nom or not extra_info or not nom_festival or not date_festival:
        messagebox.showwarning("Erreur", "Tous les champs doivent être remplis")
        return

    if type_artiste == "Musicien":
        artiste = Musicien(nom, extra_info)
    elif type_artiste == "DJ":
        artiste = DJ(nom, extra_info)

    artiste.ajouter_artiste()

    festival = Festival(nom_festival, date_festival)
    festival.ajouter_artiste(artiste)
    festival.ajouter_festival()

    text_festivals.insert(END, f"Festival: {nom_festival} - Date: {date_festival}\n")
    text_festivals.insert(END, f"  - Artiste: {nom}, Type: {type_artiste}, Info: {extra_info}\n\n")

    # Efface les champs après ajout
    entry_nom.delete(0, END)
    entry_extra.delete(0, END)
    entry_nom_festival.delete(0, END)
    entry_date_festival.delete(0, END)

creer_base_donnees()
window = Tk()
window.title("Festivals et Artistes")
window.geometry("600x700")
window.configure(background="grey")

Label(window, text="Nom du Festival:").pack(pady=5)
entry_nom_festival = Entry(window)
entry_nom_festival.pack(pady=5)

Label(window, text="Date du Festival:").pack(pady=5)
entry_date_festival = Entry(window)
entry_date_festival.pack(pady=5)

Label(window, text="Ajouter un Artiste", font=("Arial", 14)).pack(pady=10)
Label(window, text="Nom de l'Artiste:").pack(pady=5)
entry_nom = Entry(window)
entry_nom.pack(pady=5)

Label(window, text="Type:").pack(pady=5)
artiste_type = StringVar(value="Musicien")
Radiobutton(window, text="Musicien", variable=artiste_type, value="Musicien").pack()
Radiobutton(window, text="DJ", variable=artiste_type, value="DJ").pack()

Label(window, text="Instrument / Style Musical:").pack(pady=5)
entry_extra = Entry(window)
entry_extra.pack(pady=5)

Button(window, text="Ajouter l'Artiste", command=ajouter_artiste).pack(pady=10)

Label(window, text="Liste des Festivals et Artistes", font=("Arial", 14)).pack(pady=10)
text_festivals = Text(window, height=15, width=70)
text_festivals.pack(pady=10)



window.mainloop()
