"""
@file: Jouer.py
@brief Le module Jouer comporte toutes les fonctions qui permettent de modifier la grille pour jouer
"""
from Verification import *
from Types import *
from EntreesSorties import *


def plusBassePosition(data: TData, colonne: int) -> int:
    """
       @brief Trouve la position la plus basse dans une colonne où le joueur peut placer un pion.

       @param data: Les données du jeu.
       @param colonne: La colonne dans laquelle le joueur veut placer son pion.
       @return: La ligne la plus basse disponible pour placer un pion.
       """
    grille: TGrilleMat = data[0]
    joueur: TJoueur = data[1]
    joueurIA: TJoueur = data[2]
    # recupere la hauteur de la grille auquel on -1 se qui donne le numero de la derniere ligne
    hauteurGrille: int = len(grille[1]) - 1
    hauteurGrilleActuelle: int = hauteurGrille
    print("hauteur grille = ", hauteurGrille)
    i: int = hauteurGrilleActuelle
    # boucle sur la grille de bas en haut, on s'arette seulement si on tombe sur un "."
    while (grille[hauteurGrilleActuelle][colonne] != ".") | (hauteurGrilleActuelle == -1):
        if hauteurGrilleActuelle == 0:
            return -1
        # on verifie si la case sur laquelle on est est  le pion du joueur ou le pion du joueurIA
        # on decremente la ligne
        hauteurGrilleActuelle -= 1
    print("ligne : ", hauteurGrilleActuelle)
    return hauteurGrilleActuelle


def creerCoup(data: TData, joueur: TJoueur) -> TCoup:
    """
       @brief Crée un coup à partir d'un joueur et d'une colonne. Le joueur joue dans cette colonne. Place le pion le
       plus bas possible dans la colonne. 0n suppose qu'il à été vérifié avant si il restait de la place dans cette colonne.

       @param data: Les données du jeu.
       @param joueur: Le joueur effectuant le coup.
       @return: Le coup créé.
       """
    colonne: int = demanderColonne()
    ligne = plusBassePosition(data, colonne)
    if ligne != -1:
        coupActuel: TCoup = []
        pos: list[1] = [ligne, colonne]
        print("position du coup", pos)
        coupActuel.append(joueur)
        coupActuel.append(pos)
        print("coup effectué", pos)
        return coupActuel
    else:
        afficherErreurSaisieColonne(colonne)
        return creerCoup(data, joueur)




def placerPion(data: TData, coup: TCoup) -> TData:
    """
    @brief Place le pion dans une colonne et met à jour la structure de données.
    Appel de la fonction de sauvegarde pour enregistrer l'etat du jeu une fois le coup joué

    @param data: Les données du jeu.
    @param coup: Le coup à jouer.
    @return: Les données du jeu mises à jour.
    """
    grille: TGrilleMat = data[0]
    positions: list[1] = coup[1]
    print(positions)
    joueur: TJoueur = coup[0]
    # le pion du joueur est à la position 1
    pion: str = str(joueur[1])
    grille[positions[0]][positions[1]] = pion
    # inversement de la valeur du bool qui indique si c'est au joueur non IA de jouer
    data[3] = not data[3]
    victoire(grille, coup)
    sauvegarderEtatDuJeu(data)
    return data


# supme un colonne
def coupSpecial(data: TData) -> TData:
    return data


def sauvegarderEtatDuJeu(data: TData) -> None:
    """
      @brief Enregistre l'état du jeu dans la liste TsauvegardeJeu.

      @param data: Les données du jeu.
      @return: None
      """
    sauvegarde: TSauvegardeEtatJeu = []
    sauvegarde.append(data)
    return None


def revenirEnArriere() -> None:
    """
       @brief Permet au joueur de revenir à son dernier coup joué.

       @return: None
       """
    if len(TSauvegardeEtatJeu) <= 1:
        afficherErreurUndo()
    else:
        TSauvegardeEtatJeu.pop()
        TSauvegardeEtatJeu.pop()
    return None
