import sys

def affichage_menu():
    print(" \nBienvenue sur Fantome Escape ")
    print("\n1 : Nouvelle partie") 
    print("2 : Régle du jeu") 
    print("0 : Quitter")

def menu():
    choix=int(input("\nChoisissez un nombre : "))
    print()
    if choix==0 : #sortir du jeu
        sys.exit()
    elif choix==1 : #lancer le jeu
       print('ok')
    elif choix==2 : #Regle du jeu 
        print(" ------------------------------------------------------------------------------------------------------")
        print("|                                 BIENVENUE DANS FANTOME ESCAPE                                       |")
        print("|                                                                                                     |")
        print("|                                                                                                     |")
        print("|       Dans ce jeu nous avons Casper, un gentil fantome prisonnier dans un labyrinthe avec des       |")
        print("|       etres malefiques qui veulent le garder prisonnier dans le chateausper.                        |")
        print("|       Votre but, liberer Casper pour qu'il puisse retourner dans le monde des fantomes où il        |")
        print("|       fait toujours beau et où tous ses amis l’attendent.                                           |")
        print("|                                                                                                     |")
        print("|        Le probleme Casper a du mal a s'orienter, il se perd dans le labyrinthe et ne trouve         |")
        print("|        plus la sortie                                                                               |")
        print("|        De plus un grand nombre de dangers le guettent et il doit etre tres prudent.                 |")
        print("|                                                                                                     |")
        print("|                                                                                                     |")
        print("|        Dans les pieces de ce labyrinthe on peut y trouver des ennemis :                             |")
        print("|                                  - le maitre du chateau, qui renvoient Casper au debut,             |")
        print("|                                  - des Bibbendum Chamallow , qui peuvent affaiblir Casper           |")
        print("|        Mais on peut y trouver aussi des allier :                                                    |")
        print("|                                  - le savant fou, en echange d'energie vous emmener n'importe ou**  |")
        print("|                                                                        **sauf sur la case paradie   |")
        print("|       Enfin on peut aussi y trouver de l’energie qui lui permet d'avancer et faire face au ennemis  |")
        print("|                                                                                                     |")
        print("|                                                                                                     |")
        print("|       Casper se deplace d’une case a la fois et il ne peut rejoindre qu’une case accessible         |")
        print("|       directement depuis sa position,il ne peut traverser une piece pour en rejoindre une autre,    |")
        print("|       il doit s’arreter dans la case.                                                               |")
        print("|       Deplus il peut aller d'une case un autre seulement si un couloir relie ses 2 cases.           |")
        print("|                                                                                                     |")
        print("|                                                                                                     |")
        print("|       Casper possede au depart 3 pintes d’energie et est positionne dans la case reception,         |")
        print("|       5 pintes sont cacher dans le jeu                                                              |")
        print("|                                                                                                     |")
        print("|                                                                                                     |")
        print("|       Vous gagner si Casper reussi a atteindre le paradis                                           |")
        print("|       Vous perder lorsqu’il n’a plus d’energie                                                      |")
        print("|                                                                                                     |")
        print("|                                                                                                     |")
        print(" ------------------------------------------------------------------------------------------------------")
        print()

def attribution(casper_position, debut, fin,n=0):
    for i in range(debut,fin):
        if casper_position == debut :
            case_n0 = " A "
        else : 
            case_n0 = ' '+str(9-n*4)+' '
        if casper_position == (debut+1) :
            case_n1 = " A "
        elif n==0 : 
            case_n1 = " "+str(10-n*4)
        else :
            case_n1 = " "+str(10-n*4)+" " 
        if casper_position == (debut+2) :
            case_n2 = " A "
        elif n==0 : 
            case_n2 = " "+str(11-n*4)
        else :
            case_n2 = " "+str(11-n*4)+" "
        if casper_position == (debut+3) :
            case_n3 = " A "
        elif n==0 : 
            case_n3 = " "+str(12-n*4)
        else :
            case_n3 = " "+str(12-n*4)+" "
    return case_n0, case_n1, case_n2, case_n3

def print_board(casper_position,pinte):
    case_0 = " R "  
    case_13 = " P " 
    if casper_position==13:
        case_13 = ' A '
    if casper_position==0:
        case_0 = ' A '  
    print("_"*37+"\n"+" "*35)
    print(" "*11+"_"*7+" "*6+"["+case_13+"]"+" "*6+"\n"+" "*10+"|"+" "*7+"|"+" "*7+"|"+" "*9)
    for i in range(3):
        case_n0 = case_n1 = case_n2 = case_n3 = " "
        if i in [1,2]:
            print(" "*10+"|"+" "*7+"|"+" "*7+"|"+" "*9)
        if i == 0 :
            res = attribution(casper_position,9,13,i)
            case_n0, case_n1, case_n2, case_n3= res
        if i == 1 :
            res = attribution(casper_position,5,9,i)
            case_n0, case_n1, case_n2, case_n3= res
        if i == 2 :
            res = attribution(casper_position,1,5,i)
            case_n0, case_n1, case_n2, case_n3= res
        print("    ["+case_n0+"]-+-["+case_n1+"]-+-["+case_n2+"]-+-["+case_n3+"]   ")     
    print(" "*10+"|"+" "*7+"|"+" "*17)
    print(" "*11+"-["+case_0+"]-"+" "*18+"\n"+" "*35+"\n"+" "*25+"P =",pinte," "*4+"\n"+"_"*37)
    

def ask_where_to_go():
    return input('Ou aller ?\n> ')

def is_ok_to_move(casper_position,wanted_position):
    g1 = [0,1,2,3,5,6,7,8,9,10,11]
    g2 = [3,4,7,8,11,12,13]
    if int(wanted_position) in [11,7,3]:
        return True
    if casper_position in g1 :
        if int(wanted_position) in g1 :
            return True   
    if casper_position in g2 :
        if int(wanted_position) in g2 :
            return True   
    return False
    
def compteur_pinte(pinte, bonus, fantome): 
    for i in bonus : 
        if fantome == i : 
            print("Bravo vous avez reçu un bonus")
            pinte = pinte + 1
    return pinte

def perdu(pinte): 
    if pinte < 1 : 
        print(" ---------------------------------------------------")
        print("|                      PERDU                        |")
        print("|                                                   |")
        print("|                  Vous avez perdu                  |")
        print("|                                                   |")
        print("|                                                   |")
        print("|                1 : Nouvelle partie                |")
        print("|                0 : Quitter                        |")
        print(" ---------------------------------------------------")
        menu()


def victoire(fantome):
    if fantome == 13 : 
        print(" ---------------------------------------------------")
        print("|                  FELICITATION                     |")
        print("|                                                   |")
        print("|     Vous avez reussit a atteindre le paradis      |")
        print("|                                                   |")
        print("|                      BRAVO                        |")
        print(" ---------------------------------------------------")

def maitre_du_jeu(fantome,maitre):
    if fantome==maitre : 
        print(" ---------------------------------------------------")
        print("|              RETOUR A LA CASE DEPART              |")
        print("|                                                   |")
        print("|          Vous avez rencontrez le maitre           |")
        print("|                                                   |")
        print("|     Vous etes donc retour a la case depart        |")
        print(" ---------------------------------------------------")
        print()
    return fantome=0

def savant_du_jeu(fantome,savant):
    if fantome==savant:
        pinte = pinte-2
        
    return ask_where_to_go()


#MAIN 

pinte = 2
savent = 8
maitre = 10
bc = [3,5,7]
bonus_pinte= [1,6,6,9,12]

casper_position = 0
print_board(casper_position,0)
while True :
    asked_position = int(ask_where_to_go())
    
    if is_ok_to_move(casper_position,asked_position):
        casper_position = asked_position
    print_board(casper_position,0)
    
    
#TEST 

# fantome =int(input("Donne un chiffre : "))
# pinte = compteur_pinte(pinte, bonus_pinte,fantome)
# print(print_board(fantome, pinte))
# maitre_du_jeu(fantome,maitre)
# victoire(fantome)
# perdu(pinte)
# #affichage_menu()
# #menu()

    
    




   
