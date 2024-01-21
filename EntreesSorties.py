"""
@file: EntreesSorties.py
@brief EntreesSorties Le module EntreesSorties prend en charge toutes les fonctions pour lires les E/S clavier en console
"""
from Types import TData


def initialisationManueleJoueur() -> list[bool, str]:
    """
      @brief Demande à l'utilisateur s'il veut un coup spécial et son pion.

      @return: Liste contenant un booléen indiquant s'il veut un coup spécial et un caractère pour son pion.
    """
    lres = list()
    saisieBool = input("Voulez vous avoir 1 coup special au cours de la partie ? 1 oui 0 sinon")
    lres.append(bool(int(saisieBool)))
    saisiePion = input("Saisisez 1 caractere comme pion")
    lres.append(saisiePion)
    return lres


def initialisationManueleJoueurIA() -> list[bool, str, int]:
    """
       @brief Demande à l'utilisateur s'il veut que l'IA ait 1 coup spécial au cours de la partie, son pion et le niveau de difficulté.

       @return: Liste contenant un booléen indiquant s'il veut un coup spécial, un caractère pour le pion de l'IA et le niveau de difficulté.
    """
    lres = list()
    saisieBool = input("Voulez vous que l'ia ait 1 coup special au cours de la partie ? 1 oui 0 sinon")
    lres.append(bool(int(saisieBool)))
    saisiePion = input("Saisisez 1 caractere comme pion pour l'ia")
    lres.append(saisiePion)
    saisieDifficulte = input("Saisisez saisisez le niveau de difficulté")
    lres.append(int(saisieDifficulte))
    return lres


def saisirTailleMat() -> list[int]:
    """
       @brief Demande à l'utilisateur de saisir le nombre de lignes et de colonnes de la grille.

       La saisie est répétée jusqu'à ce que le format de la grille soit acceptable (nombre de lignes et colonnes > 0).

       @return: Liste contenant le nombre de lignes et de colonnes saisis.
       """
    lres: list[int] = list()
    valide = False
    while not valide:
        entreeNbLignes = input("saisir nb lignes de la grille")
        lres.append(int(entreeNbLignes))
        entreeNbColonnes = input("saisir nb colonnes de la grille")
        lres.append(int(entreeNbColonnes))
        if lres[0] <= 0 | lres[1] <= 0:
            print("Erreur : La grille ne peut pas etre sous la forme 0*X ")
            lres.clear()
        else:
            valide = True
    return lres


def afficherErreurSaisieColonne(colonne: int) -> None:
    """
       @brief Affiche un message d'erreur indiquant qu'il n'y a plus de place dans la colonne spécifiée.

       @param colonne: Le numéro de la colonne.
    """
    print("Erreur: plus de place dans la colonne n°" + str(colonne))


def afficherErreurUndo() -> None:
    """
       @brief Affiche un message indiquant qu'il est impossible de revenir en arrière.
    """
    print("Impossible de revenir en arriere")


def demanderColonne() -> int:
    """
       @brief Demande à l'utilisateur le numéro de la colonne.

       @return: Le numéro de la colonne saisi par l'utilisateur.
    """
    return int(input("le numero de la colonne"))


def afficherEtatJeu(data: TData) -> None:
    """
        @brief Affiche l'état actuel du jeu.

        @param data: Les données du jeu.
    """
    print("[    grille : \n")
    for ligne in data[0]:
        for colonne in ligne:
            print(colonne, end=" ")
        print("`\n")
    print("Joueur : " + str(data[1]))
    print("JoueurIA : " + str(data[2]))
    print("tour du joueur : " + str(data[3]) + "    ]")
    print("------------------------------")
