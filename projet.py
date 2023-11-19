tableau = { 'pinte' : [[0,1], [0,3], [1,2], [1,2], [4,1]], 
           'bib_c' : [ [0,2], [2,2], [2,3]], 
            'maitre' : [[2,1]],
            'savant' : [[4,2]],
            'fantome' : [[1,4]],
            'No' : [[0,0], [1,0], [2,0],[4,0], [3,1],[3,2],[3,3],[4,3],[0,4],[2,4],[4,4]]}
print(tableau)

def affichage_menu():
    print(" \nBienvenue sur Fantome Escape ")
    print("\n1 : Nouvelle partie") 
    print("2 : Régle du jeu") 
    print("0 : Quitter")

def menu_deplacement() :
    print(" -------------------------------------------")
    print("|          Ou voulez vous allez             |")
    print("|                                           |")
    print("|    1   :    Gauche                        |") 
    print("|    2   :    Droite                        |")
    print("|    3   :    Monter                        |")
    print("|    4   :    Descendre                     |")
    print("|                                           |")
    print("|    0  :    Quitter                        |")
    print(" -------------------------------------------")
   

def menu():
    import sys
    choix=int(input("\nChoisissez un nombre : "))
    print()
    if choix==0 : #sortir du jeu
        sys.exit()
    elif choix==1 : #lancer le jeu
        menu_deplacement()
    elif choix==2 : #Regle du jeu 
        print("Bienvenue dans Fantome escape")
        print("\nDans ce jeu nous avons Casper, un gentil fantome prisonnier dans un labyrinthe avec des etres \nmalefiques qui veulent le garder prisonnier dans le chateausper")
        print("Votre but, liberer Casper pour qu'il puisse retourner dans le monde des fantomes où il fait toujours \nbeau et où tous ses amis l’attendent")
        print("Le probleme Casper a du mal a s'orienter, il se perd dans le labyrinthe et ne trouve plus la sortie")
        print("De plus un grand nombre de dangers le guettent et il doit etre tres prudent.")
        
        print("\nDans les pieces de ce labyrinthe on peut y trouver des ennemis :")
        print("     - le maitre du chateau, qui renvoient Casper au debut, ")
        print("     - des Bibbendum Chamallow , qui peuvent affaiblir Casper")
        print("Mais on peut y trouver aussi des allier :")
        print("     - le savant fou, en echange d'energie vous emmener n'importe ou**")
        print("         **sauf sur la case paradie")
        print("Enfin on peut aussi y trouver de l’energie qui lui permet d'avancer et faire face au ennemis")
        
        print("\nCasper se deplace d’une case a la fois et il ne peut rejoindre qu’une case accessible \ndirectement depuis sa position,il ne peut traverser une piece pour en rejoindre une autre, \nil doit s’arreter dans la case.")
        print("Deplus il peut aller d'une case un autre seulement si un couloir relie ses 2 cases.")
        
        print("\nCasper possede au depart 3 pintes d’energie et est positionne dans la case reception, \n5 pintes sont cacher dans le jeu")
        
        print("\nVous gagner si Casper reussi a atteindre le paradis")
        print("Vous perder lorsqu’il n’a plus d’energie")
        print()

affichage_menu()
menu()



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
tableau = { 'pinte' : [[0,1], [0,3], [1,2], [1,2], [4,1]], 
            'bib_c' : [ [0,2], [2,2], [2,3]], 
            'maitre' : [[2,1]],
            'savant' : [[4,2]],
            'fantome' : [[1,1]],
            'no' : [[0,0], [1,0], [2,0],[4,0], [3,1],[3,2],[3,3],[4,3],[0,4],[2,4],[4,4]],
            'gauche' : [[0,1],[1,1],[2,1],[0,2],[1,2],[2,2],[0,3],[1,3],[2,3]],
            'droite' : [[2,1], [4,1], [2,2], [4,2], [2,3], [4,3]],
            'reception' : [[1,4]], 
            'paradis' : [[3,0]]}

for i in tableau.keys():
    print(i, ' : ', tableau[i])


def menu_deplacement() :
    print(" -------------------------------------------")
    print("|          Ou voulez vous allez             |")
    print("|                                           |")
    print("|    1   :    Gauche                        |") 
    print("|    2   :    Droite                        |")
    print("|    3   :    Monter                        |")
    print("|    4   :    Descendre                     |")
    print("|                                           |")
    print("|    0  :    Quitter                        |")
    print(" -------------------------------------------")

def reception_deplacement(dictionnaire,nb):
    """"Renvois ce qui ce passe quand on part de la case reception, 
            gauche => case [0:3]
            droite => case [2,3] 
        Donc on vas sur la case et on change les coordonnee du fantome.
    """
    fantome = dictionnaire['fantome']
    reception= dictionnaire['reception']
    if fantome == reception : 
        fantome=[]
        if nb == 1 : #gauche 
            fantome.append([0,3])
            print("Vous vennais d'entre dans la case ",fantome, "\nVous avez quitter la recepetion")

        elif nb == 2 : #droite
            fantome.append([2,3])
            print("Vous vennais d'entre dans la case ",fantome, "\nVous avez quitter la recepetion")
        dictionnaire['fantome']=fantome
    return dictionnaire


def monter_decendre(dictionnaire, nb): 
    gauche = dictionnaire['gauche']
    droite = dictionnaire ['droite']
    fantome = dictionnaire['fantome']
    if nb == 1 : 
        x = fantome[0]
        y = fantome[1]
        res=[x-1,y]
        fantome=[]
        fantome.append(res)
    elif nb == 2 :
        x = fantome[0]
        y = fantome[1]
        res=[x+1,y]
        fantome=[]
        fantome.append(res)

    dictionnaire['fantome']=fantome
    
def extremite(dictionnaire):
    fantome = dictionnaire['fantome']
    if fantome[0][0]==0 : #si x = 0, extremité gauche (ne peut plus aller a gauche)
        print("tu ne peut plus aller a gauche")
        return None
    elif fantome[0][0]==4 :#si x = 4, extremité droite (ne peut plus aller a droite)
        print("tu ne peut plus aller a droite ")
        return None
    else : 
        return True 


def move(dictionnaire): 
    gauche = dictionnaire['gauche']
    droite = dictionnaire ['droite']
    fantome = dictionnaire['fantome']
    print("gauche : ", gauche, "\ndroite : ", droite, "\nCasper : ", fantome)
    menu_deplacement()
    choix=int(input("\nChoisissez un nombre : "))
    print()

    if choix == 1 : #Gauche 
        reception_deplacement(dictionnaire,choix) 

    if choix == 2 : #Droite
        reception_deplacement(dictionnaire,choix) 

    if choix == 3 : #Monter
        #print(fantome[0][1])
        compteur = fantome[0][1] - 1
        print(compteur)
        if compteur <= 1 : #permet de tester si on est pres ou pas du bord!! (quand on est pres du bord ca fonctionne )
            print("vous ne pouvez plus monter, Choisissez une autre option") 
            #menu_deplacement()
            #choix==int(input("\nChoisissez un nombre : "))
               #pas fini car ca parter dans tout les sens 



        """il manque plein de chose JE VAIS MOURIRE 
        une fois qu'on choisi droite ou gauche, suffit de changer fantome[0],
        plus check si possible d'aller dans cette direction"""
        
    return dictionnaire


move(tableau)
for i in tableau.keys():
    print(i, ' : ', tableau[i])

