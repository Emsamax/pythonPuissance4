# Module Initialisation contient les fonctions qui permettent d'initialiser une partie
# avec des paramètres par défaut ou automatiques
# Initialise ensuite les structures grille, joueurs, pion, donees,
from array import array

from EntreesSorties import *
from typing import NewType, List, Any, Type, TypeAliasType

# Structure de la grille est composée :
# d'une liste ligne qui contient un entier positif repésentant le nb de ligne de la grille
# et une liste colonne qui contient un entier positif repésentant le nb de colonne de la grille
lignes = list()
colonnes = list()
type grille = list[lignes, colonnes]

# Structure d'un joueur qui est définie par :
# un boolée coupSpécial qui permet de savoir si le coup spécial à été utilisé ou non
# un pion qui est un string
pion = str
coupSecial = True
type joueur = list[coupSecial, pion]

# Structure de l'IA est la même que celle d'un joueur avec en plus son niveau de difficulté
difficulte = int
pionIA = str
coupSecialIA = bool
type joueurIA = list[coupSecialIA, pionIA, difficulte]

# Structure data représente le jeu à l'instant t
# La structure data est représentée pars :
# une grille
# un joueur qui est le joueur qui joue au puissance4
# un booléen j1tour qui inqique si c'est au joueur1 de jouer
j1tour = bool
type data = list[grille, joueur, joueurIA, j1tour]


# La fonction initialisation crée et initialise les entitées nécéssaires au fonctionnement du jeu
# si le parametre jeuRapide = True alors on initialise la partie avec des attributs par défauts
# la fonction retourne la structure de donnée data
def initialisation(jeuRapide:bool) -> TypeAliasType:
    if (jeuRapide == True):
        return data
    else:
        # demande à l'utilisateur un série d'informations pour pouvoir créer la partie

        return data
