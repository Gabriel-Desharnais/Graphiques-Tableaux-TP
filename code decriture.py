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
VERSION="0.0.0.0.0.0.3"
def question(question_a_afficher,type_de_donnees,compteur=2,limites=-1,default=''):
    """Cette fonction permet d'éffectuer une requête d'entrée à l'instar de <<input>>
    sauf qu'elle retourne la réponse dans le type demandé en argument. Elle permet
    aussi de définir un nombre seuil, une fois ce seuil dépasser elle demmandera si
    l'utilisateur veut annuler la tâche en cours(entrer un nombre négatif pour 
    désactiver cette fonction). Elle permet aussi d'imposer un nombre limites de
    tentatives après quoi elle annulera la tâche en cours (entrer un ombre négatif pour
    désactiver cette fonction). Elle permet aussi d'ajouter une valeur par défault si
    l'utilisateur entre une valeur vide<<''>>, alors c'est cette valeur qui sera considéré
    comme entrée."""
    #On devrait ajouter un truc qui permet de choisir comme type par défault string
    while True:
        compteur-=1
        limites-=1
        a=input(question_a_afficher)
        if a=='':
            a = default
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
        if limites == 0:
            #Ici un jour on devrait ajouter de quoi qui permet d'envoyer la valeur par défaut au lieu de juste annuler
            raise Exception("Annulation du procéssus (nombre limites de tentatives atteinte)")

def afficher_variables():
    """Permet d'afficher toutes les tableaux en mémoire dans le projet courant"""
    for cle in tableaux.keys():
        print(cle)

def supprimer_variable(*lvar):
    """Permet de supprimer un tableaux de la mémoire dans le projet courant"""
    if lvar== ():
        lvar=question("quelle variable voulez-vous supprimer? ",type('')).split()
    if lvar[0]=='ALL':
        global tableaux
        tableaux={}
    else:
        for var in lvar:
            if var in tableaux:
                del tableaux[var]
            else:
                print('Variable«',var,'»inexistante')

def creer_tableau(*arg):
    """Cette fonction ajoute un tableau au dictionnaire tableaux."""
    
    #Le nom donnée par l'utilisateur servira à nommée le tableau à l'interne
    if len(arg)>2:
        nom_tableau = arg[0]
        lignes = int(arg[1])+1
        colonnes = int(arg[2])
    else:
        if len(arg)>0:
            nom_tableau = arg[0]
        else:
            nom_tableau = question("Entrer le nom que vous desirez donner au tableau : ",type(''))
        #L'utilisateur doit spécifié le nombre de colonnes et de lignes que doit contenir le tableau (plus tard ça vaudrait la peine de rendre ça facultatif)
        colonnes = question("Entrer le nombre de colonnes du tableau : ",type(0))
        lignes = question("Entrer le nombre de lignes du tableau (La ligne titre ne compte pas) :",type(0))+1
    
    #Création d'un tableau numpy pouvant contenir des chaines de charactères et étant du bon format
    tableaux[nom_tableau]=np.empty((lignes,colonnes),dtype=object)
    
    
    return nom_tableau

def importer_donnees_man(nom_tableau):
    #On devrait ajouter un truc qui vérifie si <<nom_tableau>> existe dans <<tableaux>>
    #if nom_tableau in tableaux:
    colonnes=tableaux[nom_tableau].shape[1]
    lignes=tableaux[nom_tableau].shape[0]
    print("\nVous devez donner un nom à chaqu'une des",colonnes,"colonnes\n")
    for n in range(colonnes):
        tableaux[nom_tableau][0,n]=question("Le nom de la colonne "+str(n)+"\n: ",type(''))
    
    #Entrees des données dans le tableau
    for l in range(1,lignes):
        for c in range(colonnes):
            tableaux[nom_tableau][l,c]=question("Entrez la valeur "+str(l)+" de la colonne "+tableaux[nom_tableau][0,c]+": ",type(''))
    
    return nom_tableau
    
def exporter_tableau(*arg):
    if len(arg)<1:
        print("Erreur. Veuillez fournir les arguments demmandés. Utillisez la fonction «AIDE» pour plus d'information" )
        return "_Erreur"
    if len(arg)<2:
        arg+=(arg[0],)
    if arg[0] in tableaux:
        #ecriture des données dans le fichiers
        np.savetxt(arg[1],tableaux[arg[0]],fmt="%s",delimiter=',')           #ecrit le tableau en chaines de charactères dans un fichier 
        print ("Votre tableau est enregistre sous le nom <<" + arg[1] + ">>  dans le même répertoir qu'où le code se situe")
        #On devrait ajouter d'autres type d'exportation
    else:
        print(arg[0],"n'existe pas. Impossible de l'exporter")
    
    
    
    return arg[0]

def ecriture ():
    exporter_tableau(importer_donnees_man(creer_tableau()))

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
    print("Pour afficher tous les tableaux en mémoire dans le projet courant <<AFF_VARS>>")
    print("Pour supprimer un tableau de la mémoire dans le projet courant <<SUP_VAR>>")
    print("Pour créer un tableau «NOUV_TAB»")
    print("Pour transcrire toutes vos donnée manuellement vers un tableau «REMP_TAB»")
    print("Pour exporter un tableau vers un fichier «EXP_TAB»")
    
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
        'Q':quiter,
        'AFF_VARS':afficher_variables,
        'SUP_VAR':supprimer_variable,
        'NOUV_TAB':creer_tableau,
        'REMP_TAB':importer_donnees_man,
        'EXP_TAB':exporter_tableau
        }
    commande= input("Que voulez-vous faire (E: Ecrire un fichier, L: Lire un fichier, G: tracer de graphique, A: aide, Q: arret du programme): ")
    com_arg=commande.split()
    for x in range(1,len(com_arg)):
        if com_arg[x].upper().startswith("_ASK"):
            com_arg[x]=question(com_arg[x]+":",type(''))
    try:
        menu[com_arg[0].upper()](*com_arg[1:len(com_arg)])        #Ceci cherche dans le dictionnaire une fonction répertorier sous le nom de commande et essai de l'exécuter
    except KeyError:
        print("Vous n'avez pas entré une option valide.")
    except Exception as e:
        pass
        #e.args              # arguments stored in .args
    except TypeError as e:
        print("Vous avez donnez la mauvaise quantité d'argument à la fonction",e)
    main()
tableaux = {}
if __name__ == '__main__':
  main()   
