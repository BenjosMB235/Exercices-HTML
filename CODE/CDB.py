import tkinter as tk
from tkinter import simpledialog, messagebox
import random

# Initialisation des joueurs et de leurs scores
joueurs = ["Joueur 1", "Joueur 2", "Joueur 3", "Joueur 4", "Joueur 5"]
scores = {joueur: 0 for joueur in joueurs}

# Fonction pour demander à chaque joueur de choisir un nombre
def choisir_nombre(joueur):
    return simpledialog.askinteger("Choisir un nombre", f"{joueur}, veuillez choisir un nombre entre 0 et 100 :")

# Fonction pour calculer la moyenne des nombres choisis
def calculer_moyenne(nombres):
    return sum(nombres) / len(nombres)

# Fonction pour trouver le gagnant de la manche
def trouver_gagnant(moyenne, joueurs_nombres):
    differences = {joueur: abs(nombre - moyenne) for joueur, nombre in joueurs_nombres.items()}
    gagnant = min(differences, key=differences.get)
    return gagnant

# Initialisation de la fenêtre graphique
fenetre = tk.Tk()
fenetre.title("Concours de beauté")

# Fonction principale du jeu
def jeu_concours_beaute():
    while len(joueurs) > 1:
        nombres_joueurs = {}
        for joueur in joueurs:
            nombre = choisir_nombre(joueur)
            nombres_joueurs[joueur] = nombre

        moyenne = calculer_moyenne(list(nombres_joueurs.values()))
        gagnant = trouver_gagnant(moyenne, nombres_joueurs)

        if len([nombre for nombre in list(nombres_joueurs.values()) if list(nombres_joueurs.values()).count(nombre) > 1]) > 1:
            for joueur in joueurs:
                scores[joueur] -= 1
            continue

        if moyenne in list(nombres_joueurs.values()):
            for joueur in joueurs:
                if nombres_joueurs[joueur] != moyenne:
                    scores[joueur] -= 2

        if 0 in list(nombres_joueurs.values()):
            for joueur in joueurs:
                if nombres_joueurs[joueur] == 0 and joueur != gagnant:
                    gagnant = joueur

        scores[gagnant] += 1
        scores[gagnant] -= 1
        joueurs.remove(gagnant)

    messagebox.showinfo("Fin du jeu", f"Le gagnant est {joueurs[0]}!")

# Bouton pour démarrer le jeu
bouton_demarrer = tk.Button(fenetre, text="Démarrer le jeu", command=jeu_concours_beaute)
bouton_demarrer.pack()

# Boucle principale de la fenêtre
fenetre.mainloop()
