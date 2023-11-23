
#La ligne au dessu est importante 


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
    print("\n"*30)
    case_0 = " R "  
    case_13 = " P " 
    if casper_position==13:
        case_13 = ' A '
    if casper_position==0:
        case_0 = ' A '
    print("_____________________________________")
    print("                                   ")
    print("           _______      ["+case_13+"]      ")
    print("          |       |       |         ")

    for i in range(3):
        case_n0 = case_n1 = case_n2 = case_n3 = " "

        if i in [1,2]:
            print("          |       |       |         ")
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
        
    print("          |       |                 ")
    print("           -["+case_0+"]-                  ")
    print("                                    ")
    print("                         P =",pinte,"    ")
    print("_____________________________________")
    
    
    
print_board(2,3) 

   
