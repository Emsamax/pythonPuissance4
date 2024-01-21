"""! @brief Programme IHM
 @mainpage Page IHM du puissance 4
 @section Description programme IHM
 Interface utilisateur du puissance 4, l'interface se compose de
 deux sections :
   - Une partie paramètre
   - Une partie jeu

 La partie paramètre permet de modifer les valeurs par défauts du jeu,
 comme la couleur du pion du joueur (jaune ou rouge) ; la taille de la grille et le niveau de l'IA

 La partie jeu permet d'afficher la grille au cours du jeu, de lancer le jeu et de jouer son atout.

 @section Section importation
 Ce programme utilise les modules ci-dessous:
 import tkinter as tk
 from tkinter import messagebox
 from tkinter import ttk
 from PIL import ImageTk, Image
 import os
 import time
 from Jouer import jouer, data, coupSpecial
 from IA import testIAPoserPion
 from Initialisation import initialiserTGrilleMat
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import os
import time

from EntreesSorties import afficherEtatJeu
from Jouer import jouer, data, coupSpecial
from IA import testIAPoserPion, minMax
from Initialisation import initialiserTGrilleMat
from Types import TData, TCoup

# Fenêtre Tkinter
window = tk.Tk()

# liste des 3 tailles différentes de jeu
listeTaille = ["8x8", "8x7", "9x8"]

# - Grille -#
# Liste des labels de la grille qui contient les images des pions
listeLabelGrille = []

# ! Variable à modifier car init dans le fichier initialisation.py et son contenu dans des "structures"
# => il faudra importer la "structure" et se sera cet "structure" qui sera modifié
# Taille de la grille nbLigne x nbColonne

nbLigne = len(data[0])
nbColonne = len(data[0][0])
print(nbLigne, nbColonne)
# !

# - Variable de jeu -#
# Booléen, Si False => le jeu n'est pas lancé,
# Sinon Si True => le jeu est lancé
jeu = False
# Frame de la grille de jeu contenant, initialisé dans la fonction jeuInit
# - Les boutons pour poser
# - Les labels avec les pions
frameJeu = None

# Atout variable
atoutActive = False

# Liste des images des pions
here = os.getcwd()
imgPions = [
    Image.open(os.path.join(os.path.dirname(__file__),  "img/pion_jaune.jpeg")),
    Image.open(os.path.join(os.path.dirname(__file__),  "img/pion_rouge.png")),
    Image.open(os.path.join(os.path.dirname(__file__),  "img/pion_blanc.png"))
]


# --------------------------------------------------#
# (Ajouter les menus avec Undo / Redo)
def initIHM():
    """
    @brief Fonction qui initialise l'interface

    @param initMenu : Initialise le menu, on passe la fenêtre tkinter en argument
    @param Initialisation des varaibles stringVar, utiliser dans les labels de la section paramètre et section Jeu -> Atout
       Et utilisé pour leurs valeurs : la taille de la grille ; couleurs ; niveau de diffilculté
    @param parametre : Initialisation de la section paramètres
    @param jeuInit : Initialisation
    @param On utilise la méthode mainloop pour démarer l'interface
    @return: None : ne retourne pas de valeur
    """
    # Initialise un objet Tkinter
    global window
    # Configuration
    window.title("Puissance 4")
    window.geometry("960x624")

    # Initialise le menu
    initMenu(window)

    # String Variable
    # Pour Partie Paramètre
    tailleGrille = tk.StringVar(window, "8x8")
    couleurChoix = tk.StringVar(window)
    couleurChoix.set("o")  # initialiser
    niveauChoix = tk.StringVar(window)
    niveauChoix.set("1")  # initialiser

    # Partie Grille / jeu
    tour = tk.StringVar(window, "Joueur 1")
    atoutNb = tk.StringVar(window, "1")

    print(type(window))
    # Initialise la partie paramètre de l'interface
    parametre(window, tailleGrille, couleurChoix, niveauChoix)

    # Initialise la partie jeu avec la grille / les boutons de jeux (atout, lancer une partie)
    jeuInit(window, tour, atoutNb,  tailleGrille, couleurChoix, niveauChoix)

    # Affichage Interface
    window.mainloop()


def initMenu(self: tk.Tk) -> None:
    """
    @brief initMenu : Fonction d'initialisation du menu de l'interface

    @section Fonctionnement détaillé
    On retrouve 3 partie sous-menu :
     - Undo : permet de revenir en arrière, appel la fonction undo dans IHM
     - Redo : permet d'avancé vers un ancien undo, appel la fonction redo dans IHM
     - Quitter : ferme la fenêtre de jeu

    @param self: objet tkinter tk.Tkinter, fenêtre de l'interface
    @return None
    """
    menubar = tk.Menu(self)

    undoMenu = tk.Menu(menubar, tearoff=0)
    undoMenu.add_command(label="Undo", command=undo)
    menubar.add_cascade(label="Undo", menu=undoMenu)

    redoMenu = tk.Menu(menubar, tearoff=0)
    redoMenu.add_command(label="Redo", command=redo)
    menubar.add_cascade(label="Redo", menu=redoMenu)

    ExitMenu = tk.Menu(menubar, tearoff=0)
    ExitMenu.add_command(label="Quitter", command=self.quit)
    menubar.add_cascade(label="Quitter", menu=ExitMenu)

    self.config(menu=menubar)


def parametre(self: tk.Tk, tailleGrille: tk.StringVar, couleurChoix: tk.StringVar, niveauChoix: tk.StringVar) -> None:
    """
    @brief paramètre : Fonction d'initialisation de la partie paramètre de l'interface

    @section Fonctionnement détaillé
    On crée une frame principale "frame1" et on ajoute des éléments qui représente 3 grandes fonctionnalitées de paramétrages
     - une partie gestion de la taille de la grille avec une liste déroulante
     - une partie gestion de la couleur du joueur
     - une partie niveau de jeu de l'ordinateur
    À la fin de la frame on retrouve un bouton validation qui confirme la modifiécation des paramètres,
    appel la fonction validation dans IHM
    On utilise des objet tk.StringVar pour gérer le texte dynamique.

    @param self: objet tkinter tk.Tkinter, fenêtre de l'interface
    @param tailleGrille : objet tkinter tk.StringVar, taille de la grille de jeu
    @param couleurChoix : objet tkinter tk.StringVar, couleur du pion du joueur
    @param niveauChoix : objet tkinter tk.StringVar, niveau de l'IA
    @return None
    """
    frame1 = tk.Frame(self, width=262, height=525, bg="#D9D9D9")
    frame1.pack_propagate(False)
    frame1.pack(side='left', padx=20)

    # Title
    title = tk.Label(frame1, text="Paramètres", fg='black', bg="#D9D9D9", font="TkDefaultFont 28 underline")
    title.pack(padx=10, pady=10)

    # Taille Grille
    # Pour changement de la taille de la grille (label + input)
    tailleLabel = tk.Label(frame1, text="Taile de la grille", bg="#D9D9D9")
    # ComboBox (bouton déroulant)
    listeTailleGrille = ttk.Combobox(frame1, values=listeTaille, state="readonly")
    # Pack
    tailleLabel.pack(padx=10, pady=(10, 0))
    listeTailleGrille.pack(padx=10, pady=2)
    # Element par défaut : 7x6
    listeTailleGrille.current(0)
    # Relie une action au combobox
    # Permet d'ajouter dans la varaible tailleGrille la valeur du combobox
    listeTailleGrille.bind("<<ComboboxSelected>>", lambda e: tailleGrille.set(listeTailleGrille.get()))

    # Niveau de jeu
    couleurLabel = tk.Label(frame1, text="Couleur du joueur :", fg='black', bg="#D9D9D9", font="TkDefaultFont 16")
    couleurLabel.pack(anchor='w', padx=(20, 0), pady=(20, 10))
    # Radio bouton (couleur : rouge ou jaune)
    # (Ajouter les commandes plus tard de changement de couleur)
    jauneBtn = tk.Radiobutton(frame1, text="Jaune", variable=couleurChoix, value="o", bg="#D9D9D9")
    rougeBtn = tk.Radiobutton(frame1, text="Rouge", variable=couleurChoix, value="x", bg="#D9D9D9")
    # Pack
    jauneBtn.pack(anchor='w', padx=(60, 0))
    rougeBtn.pack(anchor='w', padx=(60, 0))

    # Niveau IA choix
    niveauLabel = tk.Label(frame1, text="Niveau de l'ordinateur", fg='black', bg="#D9D9D9", font="TkDefaultFont 16")
    niveauLabel.pack(anchor='w', padx=(20, 0), pady=(20, 10))
    # Radio bouton (Niveau de jeu : 1 / 2 / 3)
    # (Ajouter les commandes plus tard de changement de couleur)
    niveauBtn1 = tk.Radiobutton(frame1, text="Niveau 1", variable=niveauChoix, value="1", bg="#D9D9D9")
    niveauBtn2 = tk.Radiobutton(frame1, text="Niveau 2", variable=niveauChoix, value="2", bg="#D9D9D9")
    niveauBtn3 = tk.Radiobutton(frame1, text="Niveau 3", variable=niveauChoix, value="3", bg="#D9D9D9")
    # Pack
    niveauBtn1.pack(anchor='w', padx=(60, 0))
    niveauBtn2.pack(anchor='w', padx=(60, 0))
    niveauBtn3.pack(anchor='w', padx=(60, 0))

    # Bouton validation
    btnvalidation = tk.Button(frame1, text="Valider",
                              bg="#D9D9D9", highlightthickness=1, highlightbackground="#D9D9D9",
                              font="TkDefaultFont 16",
                              command=lambda: validationParametre(tailleGrille, couleurChoix, niveauChoix))
    btnvalidation.pack(side='bottom', padx=10, pady=(0, 40))


def jeuInit(self: tk.Tk, tour: tk.StringVar, atoutNb: tk.StringVar,  tailleGrille, couleurChoix, niveauChoix) -> None:
    """
    @brief paramètre : Fonction d'initialisation de la partie paramètre de l'interface

    @section Fonctionnement détaillé
    On crée une frame principale "frame2" et on ajoute des éléments qui représente 3 grandes fonctionnalitées de paramétrages
     - une partie affichage de la grille (*)
     - une partie gestion des commande de jeu avec le lancement du jeu et la gestion du coup spécial
    On utilise des objet tk.StringVar pour gérer le texte dynamique.

    @section (*) Détaile  partie affichage grille :
    On utilise une variable global frame "frameJeu" qui contient nxm image de pion et représente la grille de jeu.

    @param self: objet tkinter tk.Tkinter, fenêtre de l'interface
    @param tailleGrille : objet tkinter tk.StringVar, taille de la grille de jeu
    @param couleurChoix : objet tkinter tk.StringVar, couleur du pion du joueur
    @param niveauChoix : objet tkinter tk.StringVar, niveau de l'IA
    @return None
    """
    global frameJeu

    frame2 = tk.Frame(self, width=650, height=600, bg="#D9D9D9")
    frame2.pack_propagate(False)
    frame2.pack(side='right', padx=20)

    # Label Tour du Joueur (joueur ou IA)
    tourJoueurLabel = tk.Label(frame2, textvariable=tour, fg='black', bg="#D9D9D9", font="TkDefaultFont 16")
    tourJoueurLabel.pack(side='top', anchor='nw', padx=(20, 0), pady=(20, 10))

    # Frame grille de jeu
    frameJeu = tk.Frame(frame2, width=375, height=375, bg="#000")
    frameJeu.pack_propagate(False)
    frameJeu.pack(padx=20)

    # Init de la grille
    initGrille()

    # Bouton Jeu / Ajout
    # (Ajouter commande de validation des paramètre)
    btnJeu = tk.Button(frame2, text="Joueur",
                       bg="#D9D9D9",highlightthickness=1, highlightbackground="#D9D9D9",
                       font="TkDefaultFont 16", command=lambda: jouerCmd(tailleGrille, couleurChoix, niveauChoix))
    btnJeu.pack(side='left', padx=10, pady=20)
    btnAtout = tk.Button(frame2, text="Jouer Atout",
                         bg="#D9D9D9", highlightthickness=1, highlightbackground="#D9D9D9",
                         font="TkDefaultFont 16", command=lambda: jouerAtout(atoutNb))
    btnAtout.pack(side='left', padx=10, pady=20)
    btnAnnulerAtout = tk.Button(frame2, text="Annuler Atout",
                                bg="#D9D9D9", highlightthickness=1, highlightbackground="#D9D9D9",
                                font="TkDefaultFont 16", command=lambda: AnunulerJouerAtout(atoutNb))
    btnAnnulerAtout.pack(side='left', padx=10, pady=20)

    # Label nombre d'atout
    atoutTextLabel = tk.Label(frame2, text="Nombre d'atout", fg='black', bg="#D9D9D9", font="TkDefaultFont 16")
    atoutLabel = tk.Label(frame2, textvariable=atoutNb, fg='black', bg="#D9D9D9", font="TkDefaultFont 16")
    atoutTextLabel.pack(side='left', padx=(10, 1), pady=20)
    atoutLabel.pack(side='left', padx=(1, 10), pady=20)


def initGrille() -> None:
    """
    @brief initGrille : Fonction d'initialisation de la grille côté interface

    @return: None
    """
    # frameGrille : taille 375x375
    # On récupère le nombre de ligne et de colonne
    # On les converti en nombre (int)
    global nbLigne  # = int(tailleGrille.get()[0])
    global nbColonne  # = int(tailleGrille.get()[2])
    global frameJeu

    newSize = (int(375 / nbColonne), int(375 / nbLigne))

    # Récupère l'image des pions blanc
    image = imgPions[2]
    # On redimensionne l'image selon le nombre de colonne et de ligne
    image = image.resize(newSize)
    # On crée un objet ImageTk compatible avec tkinter pour l'affichage
    img = ImageTk.PhotoImage(image)

    for j in range(nbColonne):
        # frameGrille.grid_columnconfigure(j, weight=2)
        # Création du btn pour chaque colone
        # On affecte une action : poserPion, qui prend en paramètre la colonne du bouton
        # ce qui permettra de poser le pion dans la bonne colonne
        # On utilise la méthode grid pour placer les boutons dans la colonne correspondante
        tk.Button(frameJeu, text="\/", bg="#D9D9D9",
                  highlightthickness=1, highlightbackground="#000", font="TkDefaultFont 10",
                  command=lambda colonne=j: poserPion(colonne)).grid(column=j, row=0)
        listLabel = []
        for i in range(nbLigne):
            label = tk.Label(frameJeu, image=img)
            label.grid(column=j, row=i + 1)
            label.image = img
            listLabel.append(label)
        listeLabelGrille.append(listLabel)


def deleteFrameGrille() -> None:
    """
    Fonction qui vide la frame de la grille :
     - supprime les boutons pour poser les pions
     - supprimes les labels
    """
    global frameJeu
    for widget in frameJeu.winfo_children():
        widget.grid_forget()


# - Commande / action des boutons de la frame des paramètres -#
def validationParametre(tailleGrille: tk.StringVar, couleurChoix: tk.StringVar, niveauChoix: tk.StringVar) -> None:
    """
    @brief Fonction qui valide les paramètres et mets à jour les paramètres de jeu

    @section Fonctionnement détaillé


    @param tailleGrille : objet tkinter tk.StringVar, taille de la grille de jeu
    @param couleurChoix : objet tkinter tk.StringVar, couleur du pion du joueur
    @param niveauChoix : objet tkinter tk.StringVar, niveau de l'IA
    @return: none
    """
    # Il faut changer la grille de data si changement de nbLigne et nbColonne
    global listeLabelGrille
    global nbLigne
    global nbColonne
    global jeu

    # Met à jour les paramètres du jeu si le jeux n'est pas lancé
    if not jeu:
        # - Mise à jour valeur de jeu -#
        # On met à jour les variables nbLigne x nbColonne
        nbLigne = int(tailleGrille.get()[0])
        nbColonne = int(tailleGrille.get()[2])
        data[0] = initialiserTGrilleMat(nbLigne, nbColonne)

        # On met à jour la varaible couleur du joueur
        couleur = str(couleurChoix.get())
        # Si 'o' alors le joueur joue avec les jaunes et l'ia avec les rouges (cas par défaut)
        if couleur == 'o':
            data[1][1] = 'o'
            data[2][1] = 'x'
        # Sinon la couleur du joueur est rouge ('x') et l'ia avec les jaunes ('o')
        else:
            data[1][1] = 'x'
            data[2][1] = 'o'

        # On met à jour le niveau de jeu de l'IA
        data[2][2] = int(niveauChoix.get())

        # - Partie réinitialisation Grille -#
        # Vide listeLabelGrille
        listeLabelGrille = []
        # Vide la frame de la grille
        deleteFrameGrille()
        # Réinitialise la frame de la grille avec les bonnes dimensions
        initGrille()

    else:
        messagebox.showinfo("Message du jeu", "Vous ne pouvez pas modifier les paramètres du jeu pendant une partie")



# - Commande des boutons de la frame de Jeu -#
def jouerCmd(tailleGrille, couleurChoix, niveauChoix) -> None:
    """
    @brief Fonction qui lance le jeu lorsque le joueur appuie sur le btn jouer

    @section Variables globales :
     - global jeu :
     - global nbLigne
     - global nbColonne
     - global listeLabelGrille

    @section Fonctionnement détaillé :
    La fonction commence par mettre à jour l'état du jeu (varaible "jeu")
    Puis, on initialise la grille de jeu, car en cas de 2ème partie concécutive il faut réinitialisé la grille.
    C'est-à-dire, que l'on initialise la grille de la varaible "data" et la  grille de l'interface "listeLabelGrille"
    Enfin, on affiche un message de confirmation et c'est le début de la partie.
    @return: None
    """
    global jeu
    global nbLigne
    global nbColonne
    global listeLabelGrille

    if not jeu:
        jeu = True
        # Si le joueur joue pour la 2-ème fois on réinitialise l'interface
        data[0] = initialiserTGrilleMat(nbLigne, nbColonne)
        # - Partie réinitialisation Grille -#
        # Vide listeLabelGrille
        listeLabelGrille = []
        # Vide la frame de la grille
        deleteFrameGrille()
        # Réinitialise la frame de la grille avec les bonnes dimensions
        initGrille()
        # Rafraichie l'interface
        window.update()
        # Message de confirmation de début de partie
        messagebox.showinfo("Message du jeu", "Que le meilleur gagne !!")


def jouerAtout(atoutNb) -> None:
    """
    @brief Fonction qui permet d'activé l'atout
    Ne peut être activé que si le nombre d'atout est différent de 0
    @return: None
    """
    global jeu
    global atoutActive

    # jeu lancé ?
    if jeu:
        # Si l'atout n'est pas encore joué
        if atoutNb.get() == "1":
            # L'atout est activé
            atoutActive = True
            # Met le nombre d'atout à 0
            atoutNb.set("0")
        else:
            # l'atout a déjà été joué
            messagebox.showinfo("Message du jeu", "Vous n'avez plus d'atout")
    else:
        # le jeu n'a pas été lancé
        messagebox.showinfo("Message du jeu", "Lancer le jeu pour jouer votre atout")


def AnunulerJouerAtout(atoutNb) -> None:
    """
    @brief Fonction qui permet d'annuler l'utilisation de l'atout.

    @section
    Ne peut être activé que si le nombre d'atout est de 0 et si la fonction jouerAtout a été exécuté

    @params atoutNb: tk.StringVar, objet tkinter, contient le nombre d'atout du joueur
    @return: None
    """
    global atoutActive
    # Si l'atout est activé alors on le désactive sinon c'est qu'il n'est pas activé
    if atoutActive:
        # Annuler l'atout
        atoutActive = False
        atoutNb.set("1")


# -- Action des boutons de jeux de pions sur la grille --#

def changerPionCouleur(colonne: int,  ligne: int, couleur: str) -> None:
    """
    @brief Fonction changerPionCouleur permet de changer la couleur d'un pion de coordonnées (ligne, colonne)
     en un pion de couleur spécifié dans les paramètres.

    @section Variable global :
     - global listeLabelGrille : Tableau 2D de label, contenant les images des pions (même taille que la grille)
     - global nbLigne : entier, le nombre de ligne de la grille
     - global nbColonne : entier, le nombre de colonne de la grille
     - global imgPions : Tableau 1D d'objet Image de la bibliothèque Pillow

    @section Fonctionnement détaillé :
    La fonction commence par calculer la dimension "newsize" des images en fonction des lignes et colonnes
    Puis, on teste la valeur de la couleur donnée en paramètre pour récupérer la bonne image de pion
    Enfin, on redimensionne l'image, on transforme l'objet Image en un objet ImageTk compatible avec tkinter
    et on modifie la configuration et la valeur du label stocké dans la liste "listeLabelGrille".

    @param colonne: Colonne du pion (coordonée y)
    @param ligne: Linge du pion (coordonée x)
    @param couleur: Couleur du nouveau pion parmis jaune ('o'),
    rouge ('x') ou blanc ('.' ou autre) pour le cas de l'atout
    @return: None
    """
    # Appel des variable global
    global listeLabelGrille
    global nbLigne
    global nbColonne
    global imgPions

    # Définir la taille de la grille
    newSize = (int(375 / nbColonne), int(375 / nbLigne))
    # Vazribale 'j' et 'r' à modifier ?
    if couleur == 'o':
        # Ouvre l'image du pion jaune
        image = imgPions[0]
    elif couleur == 'x':
        # Ouvre l'image du pion rouge
        image = imgPions[1]
    else:
        # Utilisable pour un undo
        image = imgPions[2]

    # Redimensionner l'image
    image = image.resize(newSize)
    # On crée un objet ImageTk compatible avec tkinter pour l'affichage
    img = ImageTk.PhotoImage(image)
    # On modifie l'image dans le label
    listeLabelGrille[colonne][ligne].configure(image=img)
    listeLabelGrille[colonne][ligne].image = img


def poserPion(colonne: int) -> None:
    """
    @brief Fonction exécuté après l'activation d'un des boutons pour poser les pions '\/'

    @section Variable global :
     - global jeu : Booléen, si Vrai alors le jeu a commencé sinon le jeu n'est pas lancé
     - global atoutActive : Booléen, Vrai si un joueur veut utilisé son atout
     - global window : tk.Tkinter, objet tkinter, fenêtre de l'interface

    @section Fonctionnement détaillé :
    La fonction commence par vérifier si le jeu est lancé sinon on ne peut pas poser de pion
    et on reçoit un message d'information.
    Puis, on vérifie si le coup est un coup spécial. Si oui, on supprime les pions de la colonne.
    Ensuite, on joue le coup du joueur en appelant la fonction "jouer" qui retourne un tuple avec
    le coup du joueur (colonne et ligne sur la grille) et l'état de victoire (booléen).
    Mais si le tuple est vide alors le coup n'est pas valide et on attend le nouveau coup du joueur.
    Puis, si les vérifications sont valides, on pose le pion dans l'interface avec la fonction "changerPionCouleur"
    Et on test le cas de victoire.



    Enfin, on pose le pion du joueur puis celui de l'IA avec une des vérifications
    de victoire et de colonne pleine
    @param colonne: entier, correspond à la colonne du pion à poser
    @return: None
    """
    # Variable jeu permet de lancer le jeu en appyant sur le boutton jouer
    global jeu
    global atoutActive
    global window

    # Si le jeu est lancé alors on peut poser un pion sinon impossible
    if jeu:
        if atoutActive:
            # On joue le coup spécial (Atout) et modifie la varaible data
            coupSpecial(data, colonne)
            # On modifie le grille de l'IHM
            for i in range(len(listeLabelGrille)):
                # Change les pions de couleur par du vide (pion blanc)
                changerPionCouleur(colonne, i, '.')
            atoutActive = False

        # On joue le coup du joueur
        res = jouer(data, colonne)
        # Si le coup a pu être joué, on peut poser le pion dans la grille
        if res != ():
            # On change la couleur du pion
            changerPionCouleur(colonne, res[0], data[1][1])
            # Joueur a gagné ?
            if res[1]:
                # Si oui alors le jeu s'arrête
                jeu = False
                # Rafraîchir L'interface pour que le pion se pose avant le message
                window.update()
                # Message d'information de victoire
                messagebox.showinfo("Message de victoire", "Vous avez gagné !")
            # Au tour de l'IA
            else:
                # Le coup de l'IA, venant de l'algorithme minmax
                dernierCoup: TCoup = res[3]
                data2 = res[-1]

                #               data  , profondeur , JoueurIA    , dernierCoup
                lesCoups: list[TCoup] = []
                resIA = minMax(res[-1], 3, data2[1], dernierCoup, lesCoups)
                #le min max nous à renvoyé le pion à poser

                print("retour du min max", resIA)
                #input()

                if isinstance(resIA, tuple) and len(resIA) == 3:

                    coupAjouer: TCoup = resIA[2][1]
                    #coupIA: TCoup = coupFinal
                    print("LE COUP A JOUER")
                    print(coupAjouer)
                    coord: list[int] = coupAjouer[1]
                    ligneIA: int = coord[0]

                    colonneIA: int = coord[1]
                    print("colonne du coup à jouer IHM", colonneIA)
                    print("ligne du coup à jouer IHM", ligneIA)
                    res = jouer(data, colonneIA)
                    print("jeu apres IA")
                    afficherEtatJeu(data)
                    changerPionCouleur(colonneIA, ligneIA, res[2][1])
                    # Victoire de l'ordinateur ?
                    if res[1]:
                        # Si oui le jeu s'arrête
                        jeu = False
                        # Rafraîchir L'interface pour que le pion se pose avant le message
                        window.update()
                        # Message de victoire
                        messagebox.showinfo("Message de victoire", "L'ordinateur a gagné !")
    else:
        # message d'information : Appuier sur jouer pour lancer le jeu
        messagebox.showinfo("Message du jeu", "Vous devez lancer le jeu pour pouvoir poser un pion")

# - Fonction Undo -#
def undo():
    pass

# - Fonction Redo -#
def redo():
    pass

def fermerFenetre():
    # On supprime les images de la grille
    deleteFrameGrille()
    # On ferme la fenêtre Tkinter
    global window
    window.destroy()

#- Test IHM -#
if __name__ == "__main__":
    initIHM()
