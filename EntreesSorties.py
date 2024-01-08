# Le module EntreesSorties prend en charge toutes les fonctions pour lires les E/S clavier et fichier
# from typing import Any, Type, TypeAliasType

# from Initialisation import lignes, colonnes, data, grilleMat
# from Jouer import *
from Types import TData

# on demande à l'utilisateur si il veut un coup sepcial et son pion
def initialisationManueleJoueur() -> list[bool, str]:
    res = list()
    saisieBool = input("Voulez vous avoir 1 coup special au cours de la partie ? 1 oui 0 sinon")
    res.append(bool(int(saisieBool)))
    saisiePion = input("Saisisez 1 caractere comme pion")
    res.append(saisiePion)
    return res


# on demande à l'utilisateur si il veut que l'ia ait un coup sepcial,  son pion et le niveau de difficulté de l'ia
def initialisationManueleJoueurIA() -> list[bool, str, int]:
    res = list()
    saisieBool = input("Voulez vous que l'ia ait 1 coup special au cours de la partie ? 1 oui 0 sinon")
    res.append(bool(int(saisieBool)))
    saisiePion = input("Saisisez 1 caractere comme pion pour l'ia")
    res.append(saisiePion)
    saisieDifficulte = input("Saisisez saisisez le niveau de difficulté")
    res.append(int(saisieDifficulte))
    return res


# demande à l'utilisateur de saisir le nb de lignes et de colonnes de la grille jusqu'a ce que le format de la grille
# soit acceptable: le nombere de lignes et colonnes de doit pas etre inferieur à 0
def saisirTailleMat() -> list[int]:
    res: list[int] = list()
    valide = False
    while not valide:
        entreeNbLignes = input("saisir nb lignes de la grille")
        res.append(int(entreeNbLignes))
        entreeNbColonnes = input("saisir nb colonnes de la grille")
        res.append(int(entreeNbColonnes))
        if res[0] <= 0 | res[1] <= 0:
            print("Erreur : La grille ne peut pas etre sous la forme 0*X ")
            res.clear()
        else:
            valide = True
    return res


def afficherEtatJeu(data: TData) -> None:
    print("[    grille : \n")
    for ligne in data[0]:
        for colonne in ligne:
            print(colonne, end=" ")
        print("`\n")
    print("Joueur : " + str(data[1]))
    print("JoueurIA : " + str(data[2]))
    print("tour du joueur : " + str(data[3]) + "    ]")
