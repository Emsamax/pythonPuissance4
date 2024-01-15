# Programme principal qui contient la boucle principale du jeu
# from Jouer import *
from Initialisation import *
from EntreesSorties import *
from Jouer import *
from Types import *
from typing import TypeAlias, Type

data: TData = initialisation(True)
afficherEtatJeu(data)
gagner: bool = False
while not gagner:
    joueurActuel: TJoueur
    if data[3]:
        joueurActuel = data[1]
    else:
        joueurActuel = data[2]
    dernierCoup: TCoup = creerCoup(data, joueurActuel)
    print(" dernier coup : ", dernierCoup)
    afficherEtatJeu(placerPion(data, dernierCoup))
    if victoire(data[0], dernierCoup):
        print(" ==== Victoire joueur : ", joueurActuel, " ==== \n")
        gagner = True
