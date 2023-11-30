import sys, random
from termcolor import colored

def affichage_menu():
    print("\nBienvenue sur Fantôme Escape\n\n1 : Nouvelle partie\n2 : Régles du jeu\n0 : Quitter")
    return int(input("\nChoisissez un nombre : "))

def menu(choix):
    if choix==0 : #sortir du jeu
        sys.exit()
    if choix==2 : #Regle du jeu 
        print("-"*104+"\n|"+" "*36+"BIENVENUE DANS FANTOME ESCAPE"+" "*37+"|\n|"+" "*102+"|")
        print("|       Dans ce jeu, Casper le gentil fantôme est prisonnier dans un labyrinthe avec des               |")
        print("|       êtres maléfiques. Ces derniers veulent le garder prisonnier dans le chateausper !              |\n|"+" "*102+"|")
        print("|       Votre but: libérer Casper pour qu'il puisse retourner dans le monde des fantômes où il         |")
        print("|       fait toujours beau."+" "*76+"|\n|"+" "*102+"|")
        print("|        Dans les pièces de ce labyrinthe on peut y trouver des ennemis :                              |")
        print("|                   - Le Maitre-du-château, qui renvoie Casper au début,                               |")
        print("|                   - Des Bibbendum Chamallow, qui peuvent affaiblir Casper                            |")
        print("|                   - Le Savant-fou, qui vous téléportera au hasard                                    |\n|"+" "*102+"|")
        print("|       Enfin on peut aussi y trouver de l’énergie qui lui permet de faire face aux ennemis.           |\n|"+" "*102+"|")
        print("|       Casper se déplace d’une case à la fois et il ne peut rejoindre qu’une case accessible          |")
        print("|       directement depuis sa position, il ne peut traverser une pi2èce pour en rejoindre une autre,   |")                                                 
        print("|       de plus il peut aller d'une case un autre seulement si un couloir relie ses 2 cases.           |\n|"+" "*102+"|")
                                                                                        
        print("|       Casper possède au départ 3 pintes d’énergie et est positionne dans la case réception,          |")
        print("|       5 pintes sont cachées dans le jeu                                                              |\n|"+" "*102+"|")
        print("|       Vous gagnez si Casper reussi à atteindre le paradis                                            |")
        print("|       Vous perdez lorsqu’il n’a plus d’énergie                                                       |\n|"+" "*102+"|\n"+"-"*104)                                                                                 
        input('\nAppuyer sur une touche\n> ')
        
def create_a_print(titre, sub , body = ""):
    to_print = ("-"*53+"\n|"+" "*51+"|\n"+titre+"\n"+sub+"\n|"+" "*51+"|\n")
    if body != "" :
        to_print += (body+"\n|"+" "*51+"|\n")
    print(to_print+"-"*53)
   
def attribution(fantome, debut, fin,n=0):
    for i in range(debut,fin):
        if fantome == debut :
            case_n0 = colored(' A ', 'magenta', attrs=["blink","bold"])   
        else : 
            case_n0 = ' '+str(9-n*4)+' '
        if fantome == (debut+1) :
            case_n1 = colored(' A ', 'magenta', attrs=["blink","bold"])   
        elif n==0 : 
            case_n1 = " "+str(10-n*4)
        else :
            case_n1 = " "+str(10-n*4)+" " 
        if fantome == (debut+2) :
            case_n2 = colored(' A ', 'magenta', attrs=["blink","bold"])   
        elif n==0 : 
            case_n2 = " "+str(11-n*4)
        else :
            case_n2 = " "+str(11-n*4)+" "
        if fantome == (debut+3) :
            case_n3 = colored(' A ', 'magenta', attrs=["blink","bold"])   
        elif n==0 : 
            case_n3 = " "+str(12-n*4)
        else :
            case_n3 = " "+str(12-n*4)+" "
    return case_n0, case_n1, case_n2, case_n3

def print_board(fantome,pinte):
    case_0 = colored(' R ', 'grey',  attrs=["bold"]) 
    case_13 = colored(' P ', 'yellow',  attrs=["bold"])  
    if fantome==0:
        case_0 = colored(' A ', 'magenta', attrs=["blink","bold"])   
    print("_"*37+"\n")
    print(" "*11+"_"*7+" "*6+"["+case_13+"] 13"+"\n"+" "*10+"|"+" "*7+"|"+" "*7+"|")
    for i in range(3):
        case_n0 = case_n1 = case_n2 = case_n3 = " "
        if i in [1,2]:
            print(" "*10+"|"+" "*7+"|"+" "*7+"|")
        if i == 0 :
            res = attribution(fantome,9,13,i)
            case_n0, case_n1, case_n2, case_n3= res
        if i == 1 :
            res = attribution(fantome,5,9,i)
            case_n0, case_n1, case_n2, case_n3= res
        if i == 2 :
            res = attribution(fantome,1,5,i)
            case_n0, case_n1, case_n2, case_n3= res
        print("    ["+case_n0+"]-+-["+case_n1+"]-+-["+case_n2+"]-+-["+case_n3+"]")     
    print(" "*10+"|"+" "*7+"|")
    print(" "*11+"-["+case_0+"]-"+"\n\n"+" "*25+"P =",pinte,"\n"+"_"*37)
    
def is_ok_to_move(fantome,wanted_position):
    g1 = [0,1,2,3,5,6,7,9,10,11]
    g2 = [3,4,7,8,11,12,13]
    if wanted_position in [11,7,3]:
        return True
    if fantome in g1 :
        if wanted_position in g1 :
            return True
    if fantome in g2 :
        if wanted_position in g2 :
            return True
    print('\nImpossible de ce déplacer ici !\n')
    return False
        
def maitre_du_jeu(fantome,maitre):
    if fantome==maitre : 
        create_a_print("|            "+colored(' RETOUR A LA CASE DEPART ', 'red', attrs=["blink","bold"])+"              |",
                       "|          Vous avez rencontré le maitre            |")
        input('\nAppuyer sur une touche\n> ')
        fantome=0
    return fantome

def savant_jeu(fantome,savant):
    if fantome==savant:
        create_a_print("|               TELEPORTATION "+colored('-1', 'red', attrs=["blink","bold"])+" PINTE              |",
                       "|        Vous avez rencontré le Savant-fou          |")
        input('\nAppuyer sur une touche\n> ')
        return random.choice(range(1,13)) , -1 
    return fantome, 0 

def bib_jeu(fantome, bc):
    if fantome in bc:
        create_a_print("|                OH NON ! "+colored('-2', 'red', attrs=["blink","bold"])+" PINTES                 |",
                       "|        Vous avez rencontré un Bibbendum           |")
        input('\nAppuyer sur une touche\n>')
        return -2
    return 0

def nouveau_tour(tour):
    print("\n"*10+"Tour : ",tour)
    return 1

def ask_where_to_go(): return input('Ou aller ? (0 to q)\n> ')

def compteur_pinte(bonus_list, fantome):
    bonus = 0
    for i in bonus_list : 
        if fantome == i : 
            print("----------------------------------------------------")
            print("           Bravo vous avez reçu un bonus")
            print("----------------------------------------------------")
            bonus += 1
    return bonus

def bruit(fantome, savant, maitre, bc):
    savant = [savant-1, savant+1, savant-4,savant+4, savant-5, savant+5, savant-3, savant+3]
    maitre = [maitre-1, maitre+1, maitre-4,maitre+4, maitre-5, maitre+5, maitre-3, maitre+3]
    bc1 = [bc[0]-1, bc[0]+1, bc[0]-4,bc[0]+4, bc[0]-5, bc[0]+5, bc[0]-3, bc[0]+3]
    bc2 = [bc[1]-1, bc[1]+1, bc[1]-4,bc[1]+4, bc[1]-5, bc[1]+5, bc[1]-3, bc[1]+3]
    bc3 = [bc[2]-1, bc[2]+1, bc[2]-4,bc[2]+4, bc[2]-5, bc[2]+5, bc[2]-3, bc[2]+3]
    #-1/+1 droite/gauche ; -4/+4 dessus/dessous ; -5/+5 diagonal droite; -3/+3 diagonal gauche
    print("----------------------------------------------------")
    if fantome in bc1 or bc2 or bc3 : 
        print("          Vous sentez une odeur de marchmallo")
    if fantome in savant : 
        print("  Vous entendez le rire sardonique du savant fou   ")
    if fantome in maitre : 
        print("Vous entendez les clès du trousseau du maitre du jeu")
    print("----------------------------------------------------")
    
def perdu(pinte): 
    if pinte < 1 : 
        create_a_print("|                      "+colored('PERDU', 'red', attrs=["blink","bold"])+"                        |",
                       "|            Vous n'avez plus de pintes             |",
                       "|             Retour au menu principal              |")
        input('\nAppuyer sur une touche\n> ')
        return True

def victoire(fantome):
    if fantome == 13 : 
        create_a_print("|                  "+colored('FELICITATION', 'yellow', attrs=["blink","bold"])+"                     |",
                       "|     Vous avez reussit a atteindre le paradis      |",
                       "|                      BRAVO                        |")
        input('\nAppuyer sur une touche\n> ')
        return True 
          
def initialisation_des_positions(alea): #Si Y, positions aléatoires
    list_position = [8,10,3,5,7,1,6,6,9,12]
    if alea.upper() == '2':
        list_position = random.sample(range(1,13),10)
    return {"savant":list_position[0],"maitre":list_position[1],"bc":list_position[2:5],"pinte":list_position[5:]}
            
#PROGRAME 
while True :
    pinte = 2 #Initialisation des variables 
    casper_position = 0    
    tour = 1 
    
    menu(affichage_menu()) #Affichage du menu de choix
    
    alea = input("\nChoix de la difficulté :\n\nLevel 1 (1)\nLevel 2 (2)\n> ")
    dico_positions=initialisation_des_positions(alea) #Generation (ou non) des positions
    
    #DEBUT DE LA PARTIE
    while True :
        tour += nouveau_tour(tour) #Compteur de tours (falcutatif)
        
        pinte += compteur_pinte(dico_positions["pinte"], casper_position) #Affectation des pintes 
        bruit(casper_position, dico_positions["savant"], dico_positions["maitre"], dico_positions["bc"]) #Affichage des bruits potentiels
        
        print_board(casper_position,pinte) #Affichage du plateau
        
        #DEPLACEMENT
        while True :
            asked_position = int(ask_where_to_go()) #Demande de déplacement
            if asked_position == 0 : #Check de demande d'exit
                sys.exit()
            if  is_ok_to_move(casper_position,asked_position): #Check de déplacement valide  
                casper_position = asked_position
                break
        
        if victoire(casper_position): #Check de la victoire 
            break
        
        #Check des méchants
        r_value = savant_jeu(casper_position,dico_positions["savant"])
        casper_position = r_value[0]
        pinte += r_value[1]
        
        casper_position = maitre_du_jeu(casper_position,dico_positions["maitre"]) 

        pinte += bib_jeu(casper_position,dico_positions["bc"])
        
        if perdu(pinte): #Check de la défaite 
            break
    
