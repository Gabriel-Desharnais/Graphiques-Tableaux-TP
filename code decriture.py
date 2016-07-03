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
def question(question_a_afficher,type_de_donnees,compteur=2,annuler=True):
    """Cette fonction permet d'éffectuer une requête d'entrée à l'instar de <<input>>
    sauf qu'elle retourne la réponse dans le type demandé en argument"""
    while True:
        compteur-=1
        a=input(question_a_afficher)
        if type(0)==type_de_donnees:
            try:
                a=int(a)
                return a
            except ValueError:
                print("Vous devez entrer un entier.")
        elif type(0.0)==type_de_donnees:
            try:
                a=float(a)
                return a
            except ValueError:
                print("Vous devez entrer un nombre à virgule flotante.")
        elif type('sa')==type_de_donnees:
            try:
                a=str(a)
                return a
            except ValueError:
                print("Vous devez entrer une chaîne de charactères.")
        else:
            raise Exception("type de données inconnu")
        if compteur==0:
            compteur=1
            b=input('Voulez vous annuler le procéssus en cours? Entrez <<c>> pour annuler :')
            if b.upper()=="C":
                raise Exception("Annulation du procéssus par l'utilisateur")
def ecriture ():
    nom_fichier = question("Entrer le nom que vous desirez donner au fichier : ",type('')) #nom attribué au fichier qui sera écrit
    
    nb_liste = question("Entrer le nombre de variable à entrer dans le fichier : ",type(0)) #nombre de variable qui vont être ecrite
    colonnes=nb_liste+1
    
    nb_donnee = question("Entrer le nombre de donnees à entrer :",type(0))
        
    lignes=nb_donnee+1                                              #+1 pour la ligne de titre
    tableau=np.empty((lignes,colonnes),dtype=object)                #Création d'un tableau numpy pouvant contenir des chaines de charactères et étant du bon format
        
    #donner un nom pour chaque colonne du tableau
    print("\nVous devez donner un nom à chaqu'une des",colonnes,"colonnes\n")
    for n in range(colonnes):
        tableau[0,n]=question("Le nom de la colonne "+str(n)+"\n: ",type(''))
    
    #Entrees des données dans le tableau
    for l in range(1,lignes):
        for c in range(colonnes):
            tableau[l,c]=question("Entrez la valeur "+str(l)+" de la variable "+tableau[0,c]+": ",type(''))

    #ecriture des données dans le fichiers
    np.savetxt(nom_fichier,tableau,fmt="%s",delimiter=',')           #ecrit le tableau en chaines de charactères dans un fichier 
    
    print ("Votre est enregistre sous le nom <<" + nom_fichier + ">>  dans le même répertoir qu'où le code se situe")


    

#Lecture d'une fichier
def lecture():
    print("Vous ne pouvez ouvrir que des fichier txt ou sans extensions avec ce programme")
    nom_doc = question("Entrez le nom complet (avec l'extension) du ficihier que vous voulez lire :",type(''))

    gd = open(nom_doc, 'r')
    print(gd.read())
    gd.close()
    
    graph = question("Voulez vous en faire une graphique (O: Oui, N: Non) :",type(''))
    
    if graph.upper() == 'O':
        graphique()

#Tracer de graphique
def graphique():

    nom_doc = question("Entrez le nom complet (avec l'extension) du fichier dont vous voulez faire un graphique :",type(''))

    gd = open(nom_doc, 'r')
    print(gd.read())
    gd.close()
  
    saut= question("Combien de ligne désirez vous sauter (combien de ligne ne sont pas des données) :",type(''))
    var =np.loadtxt(nom_doc,skiprows= int(saut) ,unpack=True)
      
    x = question("Entrez le numéros de la colonne qui sera la composante X du graphique :",type(0))

    y =question("Entrez le numéros de la colonne qui sera la composante Y du graphique :",type(0))
   
    varx = var[x-1]
    vary = var[y-1]
    axe_x =question("Entrer le titre de l'axe des x :",type(''))
    axe_y = question("Entrer le titre de l'axe des y :",type(''))
    
    
    plt.plot(varx, vary)
    plt.xlabel(axe_x)
    plt.ylabel(axe_y)
       
    nom_graph = question("Entrer le nom du graphique :",type(''))
    plt.savefig(nom_graph+'.png')               #Enregitre une image <<PNG>> du graphique
    plt.show()                                  #Affiche le graphique


def aide():
    print("Ceci est le menu d'aide\n")
    print("La version du logiciel: ",VERSION,"\n")
    print("Ce programme permet à l'utilisateur d'importer les données de différentes manières et d'en faire des tableaux ou des graphiques \n")
    print("afin de créer un tableau et de l'exporter, choisisez l'option 'E' dans le menu principal. Il vous faudra ensuite entrez les données manuellement")
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
    except Exception as e:
        pass
        #e.args              # arguments stored in .args
    main()
if __name__ == '__main__':
  main()   
