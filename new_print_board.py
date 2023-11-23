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
