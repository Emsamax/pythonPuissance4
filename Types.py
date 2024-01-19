"""
    @file Types.py
    @brief Contient tous les types utilisés dans le puissance4 afin d'éviter les dépendances circulaires
"""

from array import array
from typing import TypeAlias

TGrilleMat: TypeAlias = [list[list[str]]]
"""!
    @type TGrilleMat
    @details Structure de la grille est composée d'une matrice de str de taille n*m.
    - `ligne`: liste ligne qui contient un entier positif représentant le nb de ligne de la grille.
    - `colonne`: liste colonne qui contient un entier positif représentant le nb de colonne de la grille.
"""

TJoueur: TypeAlias = list[bool, str, int]
"""!
    @type TJoueur
    @details Structure d'un joueur qui est définie par :
    - `bool`: coupSpécial qui permet de savoir si le coup spécial à été utilisé ou non.
    - `str`: pion qui est un string.
    - `int`: qui représente le niveau de difficulté  de l'ia, si = 0 alors le joueur n'est pas une ia.
"""

bJ1tour: bool = True
"""!
    @type bJ1tour
    - `bool bJ1tour`: Booleen qui indique si c'est au joueur 1 de jouer ou non.
"""

TData: TypeAlias = list[TGrilleMat, TJoueur, TJoueur, bool]
"""!
    @type TData 
    @details Structure data représente le jeu à l'instant t. La structure data est représentée par :
    - une grille.
    - un joueur qui est le joueur qui joue au puissance4.
    - booléen j1tour qui indique si c'est au joueur1 de jouer.
"""

TSauvegardeEtatJeu: TypeAlias = list[TData]
"""!
    @type TSauvegardeEtatJeu
    @details Liste qui sauvegarde tous les états du jeu : le dernier coup joué est le dernier élément de la liste.
"""

TCoup: TypeAlias = list[TJoueur, list[1]]
"""!
    @type TCoup
    @details Cet Alias représente un coup sous la forme : le joueur qui l'a joué, la ligne et la colonne du coup.
"""
