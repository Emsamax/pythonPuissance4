# Le module Verification contient toutes les fonctions de vérification qui permettent de valider si le coup
# est valide ou non.
# Fonctions de victoire et abandon

from Types import *


# verifie si il reste de la place dans la colonne passée en parametre
def verifierPosition(grille: TGrilleMat, colonne: int) -> bool:
    colonneValide: bool = False
    i: int = len(grille[1])
    while (grille[i][colonne]) != ".":
        if (i == 0):
            return colonneValide
        else:
            grille[i][colonne] = grille[i - 1][colonne]
    colonneValide = True
    return colonneValide


# renvoie True si le dernier joueur qui à joué a remporté la partie
def victoire(grille: TGrilleMat, dernierCoupJoue: TCoup) -> bool:
    if verifierVictoireColonne(grille, dernierCoupJoue) | verifierVictoireLigne(grille,
                                                                                dernierCoupJoue) | verifierVictoireDiagonale(
        grille, dernierCoupJoue):
        return True
    else:
        return False


# verifie si à partir du pion joué si il est gagnant sur la colonne
def verifierVictoireColonne(grille: TGrilleMat, dernierCoupJoue: TCoup) -> bool:
    colonneGagante: bool = False
    # la colonne du dernier coup joué se trouve TCoup[Tjoueur list[ligne, colonne]] ligne et colonne sont des int
    colonne: int = dernierCoupJoue[1][1]
    compteur: int = 0
    joueur: TJoueur = dernierCoupJoue[0]
    for i in range(colonne):
        # le caractere qui représente le pion du joueur est à la position 1 dans sa liste
        if (grille[i][colonne]) == joueur[1]:
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
    ligneGagante: bool = False
    # la ligne du dernier coup joué se trouve en [0],[0]TCoup[Tjoueur list[ligne, colonne]] ligne et colonne sont des int
    ligne: int = dernierCoupJoue[1][0]
    compteur: int = 0
    joueur: TJoueur = dernierCoupJoue[0]
    for i in range(ligne):
        # le caractere qui représente le pion du joueur est à la position 1 dans sa liste
        if (grille[ligne][i]) == joueur[1]:
            compteur += 1
            # on verifie si le compteur est égal à 4
            if compteur == 4:
                ligneGagante = True
        # cas ou le pion sur la case ou on se situe n'est pas celui du joueur qui à joué
        else:
            # on remet le compteur à 0 car il n'y a plus un suite de pion
            compteur = 0
    return ligneGagante


# verifie si à partir du pion joué si il est gagnant sur la diagonale. Comme la grille est de taille variable,
# il est impossible de gagner en diagonale si la grille est sous la forme [paire, impaire] ou [impaire, paire]
def verifierVictoireDiagonale(grille: TGrilleMat, dernierCoupJoue: TCoup) -> bool:
    diagonaleGagante1: bool = False
    diagonaleGagante2: bool = False
    lignePaire: bool = len(grille[0]) % 2
    colonnePaire: bool = len(grille[1]) % 2
    # on ne verifie les condition de victoire seulement si le nb de  lignes et de colonnes sont tous 2 pairs ou impairs
    if lignePaire & colonnePaire == True | lignePaire == False & colonnePaire == False:
        tailleLigne: int = len(grille[0])
        tailleColonne: int = len(grille[1])
        compteurDiag1: int = 0
        compteurDiag2: int = 0
        joueur: TJoueur = dernierCoupJoue[0]
        # boucle sur les lignes et colonnes de la grille
        for i in range(tailleLigne):
            for j in range(tailleColonne):
                # verification de la diagonale 1 [i][i]
                if grille[i][i] == joueur[1]:
                    compteurDiag1 += 1
                    # on verifie si le compteur de la 1 ere diagonale est égal à 4
                    if compteurDiag1 == 4:
                        diagonaleGagante1 = True
                # si on n'a pas un suite de pion du joueur qui à joué on remet le compteur à 0
                else:
                    compteurDiag1 = 0

                # verification de la diagonale 2 [tailleLigne -i - 1][i]
                if grille[tailleLigne - i - 1][i] == joueur[0]:
                    compteurDiag2 += 1
                    # on verifie si le compteur de la 2 eme diagonale est égal à 4
                    if compteurDiag1 == 4:
                        diagonaleGagante2 = True
                # si on n'a pas un suite de pion du joueur qui à joué on remet le compteur à 0
                else:
                    compteurDiag2 = 0

        # on verifie les deux diagonales en meme temps donc un ou logique permet de savoire si une des 2 diagonale est gagnante.
        return diagonaleGagante1 | diagonaleGagante2
    else:
        return False
