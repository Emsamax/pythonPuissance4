"""!
    @file Verification.py
    @brief Le module Verification contient toutes les fonctions de vérification qui permettent de valider si le coup
    est valide ou non.
"""

from Types import *
from EntreesSorties import *


# renvoie True si le dernier joueur qui à joué a remporté la partie
def victoire(grille: TGrilleMat, dernierCoupJoue: TCoup) -> bool:
    """!
        @brief Vérifie si le dernier joueur qui a joué a remporté la partie.

        @param grille: La grille du jeu.
        @param dernierCoupJoue: Les informations sur le dernier coup joué (joueur, position).
        @return: True si le dernier joueur a remporté la partie, sinon False.
        """
    if (verifierVictoireColonne(grille, dernierCoupJoue) | verifierVictoireLigne(grille, dernierCoupJoue) |
            verifierVictoireDiagonale1(grille, dernierCoupJoue) | verifierVictoireDiagonale2(grille, dernierCoupJoue)):
        return True
    else:
        return False


# verifie si à partir du pion joué si il est gagnant sur la colonne
def verifierVictoireColonne(grille: TGrilleMat, dernierCoupJoue: TCoup) -> bool:
    """!
       @brief Vérifie si le dernier joueur a gagné en colonne.

       @param grille: La grille du jeu.
       @param dernierCoupJoue: Les informations sur le dernier coup joué (joueur, position).
       @return: True si le dernier joueur a gagné en colonne, sinon False.
       """
    colonneGagante: bool = False
    # la colonne du dernier coup joué se trouve TCoup[Tjoueur list[ligne, colonne]] ligne et colonne sont des int
    colonneSaisie: int = dernierCoupJoue[1][1]
    tailleColonne: int = len(grille[1])
    print(tailleColonne)
    compteur: int = 0
    joueur: TJoueur = dernierCoupJoue[0]
    for i in range(tailleColonne):
        # le caractere qui représente le pion du joueur est à la position 1 dans sa liste
        if (grille[i][colonneSaisie]) == joueur[1]:
            compteur += 1
            # on verifie si le compteur est égal à 4
            if compteur == 4:
                colonneGagante = True
        # cas ou le pion sur la case ou on se situe n'est pas celui du joueur qui à joué
        else:
            # on remet le compteur à 0 car il n'y a plus un suite de pion
            compteur = 0
    return colonneGagante


# verifie si à partir du pion joué si il est gagnant sur la ligne
def verifierVictoireLigne(grille: TGrilleMat, dernierCoupJoue: TCoup) -> bool:
    """!
        @brief Vérifie si le dernier joueur a gagné en ligne.

        @param grille: La grille du jeu.
        @param dernierCoupJoue: Les informations sur le dernier coup joué (joueur, position).
        @return: True si le dernier joueur a gagné en ligne, sinon False.
        """
    ligneGagante: bool = False
    # la ligne du dernier coup joué se trouve en [0],[0]TCoup[Tjoueur list[ligne, colonne]] ligne et colonne sont des int
    ligneChoisie: int = dernierCoupJoue[1][0]
    tailleLigne: int = len(grille[0])
    compteur: int = 0
    joueur: TJoueur = dernierCoupJoue[0]
    for i in range(tailleLigne):
        # le caractere qui représente le pion du joueur est à la position 1 dans sa liste
        if (grille[ligneChoisie][i]) == joueur[1]:
            compteur += 1
            # on verifie si le compteur est égal à 4
            if compteur == 4:
                ligneGagante = True
        # cas ou le pion sur la case ou on se situe n'est pas celui du joueur qui à joué
        else:
            # on remet le compteur à 0 car il n'y a plus un suite de pion
            compteur = 0
    return ligneGagante


# verifie si à partir du pion joué si il est gagnant sur la diagonale.
# on verifie les diagonales partant de en haut a gauche vers en bas à droite
def verifierVictoireDiagonale1(grille: TGrilleMat, dernierCoupJoue: TCoup) -> bool:
    """!
       @brief Vérifie si le dernier joueur a gagné en diagonale (de gauche à droite).

       @param grille: La grille du jeu.
       @param dernierCoupJoue: Les informations sur le dernier coup joué (joueur, position).
       @return: True si le dernier joueur a gagné en diagonale, sinon False.
       """
    victoire: bool = False
    cordonee: list = dernierCoupJoue[1]
    joueur: TJoueur = dernierCoupJoue[0]
    pion: str = joueur[1]
    posX: int = cordonee[0]
    posY: int = cordonee[1]
    print(posX, posY)

    posXFinale: int = -1
    posYFinale: int = -1
    # on cherche la case la plus en haut à gauche du dernier coup joué à max de 3 cases
    for i in range(3):
        if ((posX) >= 1) & ((posY) >= 1):
            posX -= 1
            posY -= 1
            print("position diagonale haut gauche : ", posX, posY, " tour de boucle : ", i)
        # je peux aller à gauche?
        # if posY - 1 >= 0:
        #    posY -= 1
        #    # si oui je monte
        #    if posX - 1 > 0:
        #        posX -= 1
    print("position diagonale haut gauche : ", posX, posY)
    posXFinale = posX
    posYFinale = posY
    # on part de la position la plus en haut à gauche de la diagonale
    # on boucle jusqu'a sortire de la grille
    distance: int = 0
    compteur: int = 0
    positionActuelleX: int = posXFinale
    positionActuelleY: int = posYFinale
    while (positionActuelleX + distance < len(grille[0])) & (positionActuelleY + distance < len(grille[1])):
        if grille[positionActuelleX + distance][positionActuelleY + distance] == pion:
            compteur += 1
            print("================================ compteur gauche à droite : ", compteur)
            # il y a deja le pion joué dans la diagonale
            if compteur == 4:
                victoire = True
        else:
            compteur = 0
        distance += 1
    return victoire


# verifie si à partir du pion joué si il est gagnant sur la diagonale.
# on verifie les diagonales partant de en haut a droite vers en bas à gauche
def verifierVictoireDiagonale2(grille: TGrilleMat, dernierCoupJoue: TCoup) -> bool:
    """!
       @brief Vérifie si le dernier joueur a gagné en diagonale (de gauche à droite).

       @param grille: La grille du jeu.
       @param dernierCoupJoue: Les informations sur le dernier coup joué (joueur, position).
       @return: True si le dernier joueur a gagné en diagonale, sinon False.
       """
    victoire: bool = False
    cordonee: list = dernierCoupJoue[1]
    joueur: TJoueur = dernierCoupJoue[0]
    pion: str = joueur[1]
    posX: int = cordonee[0]
    posY: int = cordonee[1]
    print(posX, posY)

    posXFinale: int = -1
    posYFinale: int = -1
    # on cherche la case la plus en haut à  droite du dernier coup joué à max de 3 cases
    for i in range(3):
        if (posX>=1) & ((posY) < len(grille[1])-1):
            posX -= 1
            posY += 1
        # je peux aller à droite?
        # if posY + 1 < len(grille[1]):
        #   posY += 1
        #    # si oui je monte
        #    if posX - 1 > 0:
        #       posX -= 1
    posXFinale = posX
    posYFinale = posY

    print("coordonees haut diagonale droite : ", posXFinale, posYFinale)
    distance: int = 0
    compteur: int = 0
    positionActuelleX: int = posXFinale
    positionActuelleY: int = posYFinale
    # parcour de la diagonale en haut a droite vers en bas a gauche
    while (positionActuelleX + distance < len(grille[0])) & (positionActuelleY - distance >= 0):
        print("distance", distance)
        print(positionActuelleX + distance, positionActuelleY - distance)
        if grille[positionActuelleX + distance][positionActuelleY - distance] == pion:
            compteur += 1
            print("================================ compteur droite à gauche : ", compteur)
            # il y a deja le pion joué dans la diagonale
            if compteur == 4:
                victoire = True
        else:
            compteur = 0
        distance += 1
    return victoire
