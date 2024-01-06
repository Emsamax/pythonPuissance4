# Le module EntreesSorties prend en charge toutes les fonctions pour lires les E/S clavier et fichier
#from typing import Any, Type, TypeAliasType

#from Initialisation import lignes, colonnes, data, grilleMat
from Jouer import *


# Demande à l'utilisateur de rentrer la largeur de la grille, la hauteur de la grille, son caractere pion.
# Le char pour le pion de l'IA et le niveau de difficulté de l'IA.
def initData() -> list:
    data = list()
    data.append(input("nb ligne\n"))
    data.append(input("nb colonnes\n"))
    data.append(input("char pour le pion\n"))
    data.append(input("char pour le pion de l'IA"))
    data.append(input("niveau de difficulltée de l'IA"))
    return data


#def afficherJeu(data: data, grille: grilleMat) -> None:
    #for ligne in grille:
        #print(' | '.join(str(cellule) for cellule in ligne))
        #print("-" * (lignes* 4 - 1))  # Ligne de séparation

    #print(data[2])
    #print(data[3])
    #print("tour du joueur " + data[4])
