# Le module Verification contient toutes les fonctions de vérification qui permettent de valider si le coup
# est valide ou non.
# Fonctions de victoire et abandon

from Types import *
from EntreesSorties import *






# renvoie True si le dernier joueur qui à joué a remporté la partie
def victoire(grille: TGrilleMat, dernierCoupJoue: TCoup) -> bool:
    diagonaleGagante1: bool = False
    diagonaleGagante2: bool = False
    lignePaire: bool = bool(len(grille[0]) % 2)
    colonnePaire: bool = bool(len(grille[1]) % 2)
    # on ne verifie les condition de victoire en diagonal seulement si le nb de  lignes et de colonnes sont tous 2 pairs ou impairs
    # if lignePaire & colonnePaire | lignePaire == False & colonnePaire == False:
    # if verifierVictoireColonne(grille, dernierCoupJoue) | verifierVictoireLigne(grille,
    #                                                                             dernierCoupJoue) #| verifierVictoireDiagonale(
    #      grille, dernierCoupJoue):
    #       return True
    #    else:
    #         return False
    # else:
    if verifierVictoireColonne(grille, dernierCoupJoue) | verifierVictoireLigne(grille, dernierCoupJoue):
        return True
    else:
        return False


# verifie si à partir du pion joué si il est gagnant sur la colonne
def verifierVictoireColonne(grille: TGrilleMat, dernierCoupJoue: TCoup) -> bool:
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


# verifie si à partir du pion joué si il est gagnant sur la diagonale. Comme la grille est de taille variable,
# il est impossible de gagner en diagonale si la grille est sous la forme [paire, impaire] ou [impaire, paire]
def verifierVictoireDiagonale1(grille: TGrilleMat, dernierCoupJoue: TCoup) -> bool:
    tailleLigne: int = len(grille[0])
    tailleColonne: int = len(grille[1])
    compteurDiag1: int = 0
    compteurDiag2: int = 0
    joueur: TJoueur = dernierCoupJoue[0]
    ligneChoisie: int = dernierCoupJoue[1][0]
    colonneChoisie: int = dernierCoupJoue[1][1]
    diagonaleGagante1: bool = False
    diagonaleGagante2: bool = False
    ligneActuelle: int = tailleLigne
    colonneActuelle: int = tailleColonne
    joueur: str = dernierCoupJoue[0][1]
    # boucle sur les lignes et colonnes de la grille à partir de la position du dernier coup joué
    # si un pion A(x, y) on teste (x+n, y-n), (x-n, y+n), (x+n, y+n) et (x-n, y-n) avec n <=3
    # si dans une direction x-n n'est plus dans la grille stop le test de la direction
    # a chaque incrementation on fait la somme des 2 compteurs pour les 2 directions qui constituent une diagonale
    # et on regarde si la somme >= 4
    i = 1
    for i in range(3):
        # diagonale1 direction (x-1, y+1)
        pos1: list = dernierCoupJoue[1]
        if (pos1[0] + i) <= tailleLigne:
            pos1[1] -= i

        # diagonale1 direction (x+1, y-1)
        pos2: list = dernierCoupJoue[1]
        pos2[0] += i
        pos2[1] -= i
        # if verifierPion(pos1, joueur, grille):
        #   diagonaleGagante1 += 1
        # elif verifierPion(pos2, joueur, grille):
        #  diagonaleGagante1 += 1

        # diagonale2 direction (x+1, y+1)
        pos3: list = dernierCoupJoue[1]
        pos3[0] += i
        pos3[1] -= i

        # diagonale2 direction (x-1, y-1)
        pos4: list = dernierCoupJoue[1]
        pos4[0] += i
        pos4[1] -= i
    # on verifie les deux diagonales en meme temps donc un ou logique permet de savoire si une des 2 diagonale
    # est gagnante.
    return diagonaleGagante1 | diagonaleGagante2

# def verifierPion(coordoneePion: list, joueur: str, grille: TGrilleMat) -> bool:
#   pos: list = coup[1]
#  pion = coup[0][1]
# if grille[pos[0]][pos[1]] == pion:
#    return True
# else:
#   return False
