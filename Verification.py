"""!
    @file Verification.py
    @brief Le module Verification contient toutes les fonctions de vérification qui permettent de valider si le coup
    est valide ou non.
"""

from Types import *
from EntreesSorties import *


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


def verifierVictoireColonne(grille: TGrilleMat, dernierCoupJoue: TCoup) -> bool:
    """!
       @brief Vérifie si le dernier joueur a gagné en colonne.

       @param grille: La grille du jeu.
       @param dernierCoupJoue: Les informations sur le dernier coup joué (joueur, position).
       @return: True si le dernier joueur a gagné en colonne, sinon False.
       """
    bcolonneGagante: bool = False
    # la colonne du dernier coup joué se trouve TCoup[Tjoueur list[ligne, colonne]] ligne et colonne sont des int
    icolonneSaisie: int = dernierCoupJoue[1][1]
    itailleColonne: int = len(grille[1])
    icompteur: int = 0
    Tjoueur: TJoueur = dernierCoupJoue[0]
    for uiboucle in range(itailleColonne):
        # le caractere qui représente le pion du joueur est à la position 1 dans sa liste
        if (grille[uiboucle][icolonneSaisie]) == Tjoueur[1]:
            icompteur += 1
            # on verifie si le icompteur est égal à 4
            if icompteur == 4:
                bcolonneGagante = True
        # cas ou le pion sur la case ou on se situe n'est pas celui du joueur qui à joué
        else:
            # on remet le icompteur à 0 car il n'y a plus un suite de pion
            icompteur = 0
    return bcolonneGagante


def verifierVictoireLigne(grille: TGrilleMat, dernierCoupJoue: TCoup) -> bool:
    """!
        @brief Vérifie si le dernier joueur a gagné en ligne.

        @param grille: La grille du jeu.
        @param dernierCoupJoue: Les informations sur le dernier coup joué (joueur, position).
        @return: True si le dernier joueur a gagné en ligne, sinon False.
        """
    bligneGagante: bool = False
    iligneChoisie: int = dernierCoupJoue[1][0]
    tailleLigne: int = len(grille[0])
    icompteur: int = 0
    Tjoueur: TJoueur = dernierCoupJoue[0]
    for uiboucle in range(tailleLigne):
        # le caractere qui représente le pion du joueur est à la position 1 dans sa liste
        if (grille[iligneChoisie][uiboucle]) == Tjoueur[1]:
            icompteur += 1
            # on verifie si le icompteur est égal à 4
            if icompteur == 4:
                bligneGagante = True
        # cas ou le pion sur la case ou on se situe n'est pas celui du joueur qui à joué
        else:
            # on remet le icompteur à 0 car il n'y a plus un suite de pion
            icompteur = 0
    return bligneGagante

def verifierVictoireDiagonale1(grille: TGrilleMat, dernierCoupJoue: TCoup) -> bool:
    """!
       @brief Vérifie si le dernier joueur a gagné en diagonale (de gauche à droite).

       @param grille: La grille du jeu.
       @param dernierCoupJoue: Les informations sur le dernier coup joué (joueur, position).
       @return: True si le dernier joueur a gagné en diagonale, sinon False.
       """
    victoire: bool = False
    cordonee: list = dernierCoupJoue[1]
    Tjoueur: TJoueur = dernierCoupJoue[0]
    spion: str = Tjoueur[1]
    iposX: int = cordonee[0]
    iposY: int = cordonee[1]

    iposXFinale: int = -1
    iposYFinale: int = -1
    # on cherche la case la plus en haut à gauche du dernier coup joué à max de 3 cases
    for uiboucle in range(3):
        if ((iposX) >= 1) & ((iposY) >= 1):
            iposX -= 1
            iposY -= 1
    iposXFinale = iposX
    iposYFinale = iposY
    # on part de la position la plus en haut à gauche de la diagonale
    # on boucle jusqu'a sortire de la grille
    idistance: int = 0
    icompteur: int = 0
    iipositionActuelleXpion: int = iposXFinale
    positionActuelleY: int = iposYFinale
    while (iipositionActuelleXpion + idistance < len(grille[0])) & (positionActuelleY + idistance < len(grille[1])):
        if grille[iipositionActuelleXpion + idistance][positionActuelleY + idistance] == spion:
            icompteur += 1
            if icompteur == 4:
                victoire = True
        else:
            icompteur = 0
        idistance += 1
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
    Tjoueur: TJoueur = dernierCoupJoue[0]
    spion: str = Tjoueur[1]
    iposX: int = cordonee[0]
    iposY: int = cordonee[1]

    iposXFinale: int = -1
    iposYFinale: int = -1
    # on cherche la case la plus en haut à  droite du dernier coup joué à max de 3 cases
    for uiboucle in range(3):
        if (iposX>=1) & ((iposY) < len(grille[1])-1):
            iposX -= 1
            iposY += 1
    iposXFinale = iposX
    iposYFinale = iposY

    idistance: int = 0
    icompteur: int = 0
    iipositionActuelleXpion: int = iposXFinale
    positionActuelleY: int = iposYFinale
    # parcour de la diagonale en haut a droite vers en bas a gauche
    while (iipositionActuelleXpion + idistance < len(grille[0])) & (positionActuelleY - idistance >= 0):
        if grille[iipositionActuelleXpion + idistance][positionActuelleY - idistance] == spion:
            icompteur += 1
            if icompteur == 4:
                victoire = True
        else:
            icompteur = 0
        idistance += 1
    return victoire
