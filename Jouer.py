"""
@file: Jouer.py
@brief Le module Jouer comporte toutes les fonctions qui permettent de modifier la grille pour jouer
"""
from Verification import *
from Types import *
from EntreesSorties import *
from Initialisation import *


# -- Varibale Global Initialisation --#
data: TData = initialisation(True)


def jouer(data: TData, icolonne: int) -> tuple:
    bgagner = False
    joueurActuel: TJoueur
    if data[3]:
        joueurActuel = data[1]
    else:
        joueurActuel = data[2]
    if not testColonnePleine(data[0], icolonne):
        dernierCoup: TCoup = creerCoup(data, joueurActuel, icolonne)
        #afficherEtatJeu(placerPion(data, dernierCoup))
        nvTData: TData = placerPion(data, dernierCoup)
        if victoire(data[0], dernierCoup):
            print(" ==== Victoire joueur : ", joueurActuel, " ==== \n")
            bgagner = True

        return dernierCoup[1][0], bgagner, joueurActuel, dernierCoup, nvTData
    return ()


def testColonnePleine(grille: TGrilleMat, icolonne: int):
    """
        @brief verifie si la colonne est pleine
        @params colonne
        @params grille
        @return True si la colonne est pleine
    """
    if grille[0][icolonne] != ".":
        return True
    return False


def plusBassePosition(data: TData, icolonne: int) -> int:
    """
       @brief Trouve la position la plus basse dans une colonne où le joueur peut placer un pion.

       @param data: Les données du jeu.
       @param colonne: La colonne dans laquelle le joueur veut placer son pion.
       @return: La ligne la plus basse disponible pour placer un pion.
       """
    grille: TGrilleMat = data[0]
    # recupere la hauteur de la grille auquel on -1 se qui donne le numero de la derniere ligne
    ihauteurGrille: int = len(grille) - 1
    ihauteurGrilleActuelle: int = ihauteurGrille
    #print("hauteur grille = ", ihauteurGrille)
    # boucle sur la grille de bas en haut, on s'arette seulement si on tombe sur un "."
    while (grille[ihauteurGrilleActuelle][icolonne] != ".") | (ihauteurGrilleActuelle == -1):
        if ihauteurGrilleActuelle == 0:
            return -1
        # on verifie si la case sur laquelle on est est  le pion du joueur ou le pion du joueurIA
        # on decremente la ligne
        ihauteurGrilleActuelle -= 1
    #print("ligne : ", ihauteurGrilleActuelle)
    return ihauteurGrilleActuelle


def creerCoup(data: TData, joueur: TJoueur, icolonne: int) -> TCoup:
    """
       @brief Crée un coup à partir d'un joueur et d'une colonne. Le joueur joue dans cette colonne. Place le pion le
       plus bas possible dans la colonne. 0n suppose qu'il à été vérifié avant si il restait de la place dans cette colonne.

       @param data: Les données du jeu.
       @param joueur: Le joueur effectuant le coup.
       @return: Le coup créé.
    """
    ligne = plusBassePosition(data, icolonne)
   # print("LIGNE : ", ligne)
    if ligne != -1:
        coupActuel: TCoup = []
        pos: list[1] = [ligne, icolonne]
        #print("position du coup", pos)
        coupActuel.append(joueur)
        coupActuel.append(pos)
        #print("coup effectué", pos)
        return coupActuel
    return []


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
def coupSpecial(data: TData, colonne: int) -> None:
    """
    @brief suprimme tous les pions d'une colonne
    @param data:
    @param colonne:
    @return: None
    """
    for uiboucle in range(len(data[0])):
        data[0][uiboucle][colonne] = '.'
    return None


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
