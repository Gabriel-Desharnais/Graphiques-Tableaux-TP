#!/usr/bin/python3
#-utf-8
'''
Auteur: Olivier Bernard & Gabriel Desharnais
Date : 26 avril 2016
Entree: Clavier
Sortie: Moniteur
Programme: Programme pour ecrire des fichiers
           Programme pour lire des fichiers
           Programme pour tracer un graphique avec deux variables
'''

import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
import sys
import unicodedata
VERSION="0.0.0.0.0.0.2"
def ecriture ():
    nom_fichier = input("Entrer le nom que vous desirez donner au fichier : ") #nom attribué au fichier qui sera écrit
#Le <<try / except>> devrait être remplacer par une boucle qui vérifie que le nombre est convenable
    try:
        nb_liste = int((input("Entrer le nombre de variable à entrer dans le fichier : "))) #nombre de variable qui vont être ecrite
    except ValueError:
        print("Il y a une erreur, veuillez entrez un nombre entier")                               #S'assurer que le nombre est valide
        nb_liste = int(input("Entrer le nombre de variable à entrer dans le fichier: "))
    colonnes=nb_liste+1
    
   #l'ensemble du reste du code devrait se servir de tableau numpy
    if int(nb_liste) <= 3 :
        #devrait être dans une boucle
        try:
            nb_donnee = int(input("Entrer le nombre de donnees à entrer :"))
        except ValueError:
            print("Il y a une erreur, veuillez entrez un nombre entier")
            nb_donnee = int(input("Entrer le nombre de donnees à entrer :"))
        
        lignes=nb_donnee+1                                  #+1 pour la ligne de titre
        tableau=np.empty((lignes,colonnes),dtype=object)         #Création d'un tableau numpy pouvant contenir des chaines de charactères et étant du bon format
        
        #donner un nom pour chaque colonne du tableau
        print("\nVous devez donner un nom à chaqu'une des",colonnes,"colonnes\n")
        for n in range(colonnes):
            tableau[0,n]=input("Le nom de la colonne "+str(n)+"\n: ")
       
        
        #Entrees des données dans le tableau
        for l in range(1,lignes):
            for c in range(colonnes):
                tableau[l,c]=input("Entrez la valeur "+str(l)+" de la variable "+tableau[0,c]+": ")
                
        
        #ecriture des données dans le fichiers
        np.savetxt(nom_fichier,tableau,fmt="%s")           #ecrit le tableau en chaines de charactères dans un fichier 
        
        print ("Votre est enregistre sous le nom <<" + nom_fichier + ">>  dans le même répertoir qu'où le code se situe")


    

#Lecture d'une fichier
def lecture():
    print("Vous ne pouvez ouvrir que des fichier txt ou sans extensions avec ce programme")
    nom_doc = input("Entrez le nom complet (avec l'extension) du ficihier que vous voulez lire :")

    gd = open(nom_doc, 'r')
    print(gd.read())
    gd.close()
    
    graph = input("Voulez vous en faire une graphique (O: Oui, N: Non) :")
    
    if graph == 'O' or graph == 'o':
        graphique()

    if graph == 'N' or graph == 'n':
        main() # retour au main
        
#Tracer de graphique
def graphique():

    nom_doc = input("Entrez le nom complet (avec l'extension) du fichier dont vous voulez faire un graphique :")

    gd = open(nom_doc, 'r')
    print(gd.read())
    gd.close()
  
    saut= input("Combien de ligne désirez vous sauter (combien de ligne ne sont pas des données) :")
    var =np.loadtxt(nom_doc,skiprows= int(saut) ,unpack=True)
      
    try:
         x = int(input("Entrez le numéros de la colonne qui sera la composante X du graphique :"))
    except ValueError:
         print("Il y a une erreur, veuillez le numéros de la variable")
         x = int(input("Entrez le numéros de la colonne qui sera la composante X du graphique :"))

    try:
         y = int(input("Entrez le numéros de la colonne qui sera la composante Y du graphique :"))
    except ValueError:
         print("Il y a une erreur, veuillez entrer le numéros de la variable")
         y = int(input("Entrez le numéros de la colonne qui sera la composante Y du graphique :"))

    varx = var[x-1]
    vary = var[y-1]
    axe_x = input("Entrer le titre de l'axe des x :")
    axe_y = input("Entrer le titre de l'axe des y :")
    
    
    plt.plot(varx, vary)
    plt.xlabel(axe_x)
    plt.ylabel(axe_y)
       
    nom_graph = input ("Entrer le nom du graphique :")
    plt.savefig(nom_graph+'.png')
    plt.show()

    main() # retour au main    

def aide():
    print("Ceci est le menu d'aide\n")
    print("La version du logiciel: ",VERSION,"\n")
    print("Ce programme permet à l'utilisateur d'importer les données de différentes manières et d'en faire des tableaux ou des graphiques \n")
    print("Pour Importer vos données depuis un fichier: choisisez l'option 'L' dans le menu principal")        
    
def quiter():
    exit()

#main, choix entre les différentes options
def main():
    #Créer le menu à l'aide d'un dictionnaire qui contient les fonctions
    menu={
        'E':ecriture,
        'L':lecture,
        'G':graphique,
        'A':aide,
        'Q':quiter
        }
    commande= input("Que voulez-vous faire (E: Ecrire un fichier, L: Lire un fichier, G: tracer de graphique, A: aide, Q: arret du programme): ")
    try:
        menu[commande.upper()]()        #Ceci cherche dans le dictionnaire une fonction répertorier sous le nom de commande et essai de l'exécuter
    except KeyError:
        print("Vous n'avez pas entré une option valide.")
    main()
if __name__ == '__main__':
  main()   
