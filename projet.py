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

def menu():
    import sys
    choix=int(input("\nChoisissez un nombre : "))
    print()
    if choix==0 : #sortir du jeu
        sys.exit()
    elif choix==1 : #lancer le jeu
        print("ok")
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