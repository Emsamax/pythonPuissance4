# Le module Jouer comporte toutes les fonctions qui permettent de modifier la grille pour jouer
from Verification import *
from Types import *
from EntreesSorties import *
from Initialisation import *

# -- Varibale Global Initialisation --#
data: TData = initialisation(True)

def jouer (data: TData, colonne: int) -> tuple:
    gagner = False
    joueurActuel: TJoueur
    if data[3]:
        joueurActuel = data[1]
    else:
        joueurActuel = data[2]
    if not testColonnePleine(data[0], colonne):
        dernierCoup: TCoup = creerCoup(data, joueurActuel, colonne)
        afficherEtatJeu(placerPion(data, dernierCoup))
        if victoire(data[0], dernierCoup):
            print(" ==== Victoire joueur : ", joueurActuel, " ==== \n")
            gagner = True

        return dernierCoup[1][0], gagner
    return ()


def testColonnePleine(grille, colonne: int):
    if grille[0][colonne] != ".":
        return True
    return False


def plusBassePosition(data: TData, colonne: int) -> int:
    grille: TGrilleMat = data[0]
    # recupere la hauteur de la grille auquel on -1 se qui donne le numero de la derniere ligne
    hauteurGrille: int = len(grille) - 1
    hauteurGrilleActuelle: int = hauteurGrille
    print("hauteur grille = ", hauteurGrille)
    # boucle sur la grille de bas en haut, on s'arette seulement si on tombe sur un "."
    while (grille[hauteurGrilleActuelle][colonne] != ".") | (hauteurGrilleActuelle == -1):
        if hauteurGrilleActuelle == 0:
            return -1
        # on verifie si la case sur laquelle on est est  le pion du joueur ou le pion du joueurIA
        # on decremente la ligne
        hauteurGrilleActuelle -= 1
    print("ligne : ", hauteurGrilleActuelle)
    return hauteurGrilleActuelle


# crée un coup à partir d'un joueur et d'une colonne = le joueur joue dans cette colonne
# place le pions le plus bas possible dans la colonne
# on suppose q'il à été vérifié avant si il restait de la place dans cette colonne
def creerCoup(data: TData, joueur: TJoueur, colonne: int) -> TCoup:
    ligne = plusBassePosition(data, colonne)
    print("LIGNE : ", ligne)
    if ligne != -1:
        coupActuel: TCoup = []
        pos: list[1] = [ligne, colonne]
        print("position du coup", pos)
        coupActuel.append(joueur)
        coupActuel.append(pos)
        print("coup effectué", pos)
        return coupActuel
    return []
    #afficherErreurSaisieColonne(colonne)
    #return creerCoup(data, joueur, colonne)



# place le pion dans une colonne et met a jour la structure data
# Appel de la fonction de sauvegarde pour enregistrer l'etat du jeu une fois le coup joué
def placerPion(data: TData, coup: TCoup) -> TData:
    grille: TGrilleMat = data[0]
    positions: list[1] = coup[1]
    print("position : ", positions)
    joueur: TJoueur = coup[0]
    # le pion du joueur est à la position 1
    #print("test : ", joueur)
    pion: str = str(joueur[1])
    grille[positions[0]][positions[1]] = pion
    # inversement de la valeur du bool qui indique si c'est au joueur non IA de jouer
    data[3] = not data[3]
    victoire(grille, coup)
    sauvegarderEtatDuJeu(data)
    return data


# supme un colonne
def coupSpecial(data: TData, colonne: int) -> None:
    for i in range(len(data[0])):
        data[0][i][colonne] = '.'
    return None


# enregistre l'etat du jeu dans la liste TsauvegardeJeu
def sauvegarderEtatDuJeu(data: TData) -> None:
    sauvegarde: TSauvegardeEtatJeu = []
    sauvegarde.append(data)
    return None


# permet au joueur de revenir à son dernier coup joué
def revenirEnArriere() -> None:
    if len(TSauvegardeEtatJeu) <= 1:
        afficherErreurUndo()
    else:
        TSauvegardeEtatJeu.pop()
        TSauvegardeEtatJeu.pop()
    return None
