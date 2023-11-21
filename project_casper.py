import numpy as np

casper_position = 6

def print_board(casper_position):
    case_0 = "R"
    case_13 = "P"
    if casper_position==13:
        case_13 = 'A'
    if casper_position==0:
        case_0 = 'A'

    print("_____________________________")
    print("|                           |")
    print("|        _____     ["+case_13+"]      |")
    print("|       |     |     |       |")

    for i in range(3):
        case_n0 = " "
        case_n1 = " "
        case_n2 = " "
        case_n3 = " "
        if i in [1,2]:
            print("|       |     |     |       |")
        if casper_position in list(range(9,13)):
            if i == 0 :
                if casper_position == 9 :
                    case_n0 = "A"
                if casper_position == 10 :
                    case_n1 = "A"
                if casper_position == 11 :
                    case_n2 = "A"
                if casper_position == 12 :
                    case_n3 = "A"
        if casper_position in list(range(5,9)):
            if i == 1 :
                if casper_position == 5:
                    case_n0 = "A"
                if casper_position == 6 :
                    case_n1 = "A"
                if casper_position == 7 :
                    case_n2 = "A"
                if casper_position == 8 :
                    case_n3 = "A"
        if casper_position in list(range(1,5)):
            if i == 2 :
                if casper_position == 1 :
                    case_n0 = "A"
                if casper_position == 2 :
                    case_n1 = "A"
                if casper_position == 3 :
                    case_n2 = "A"
                if casper_position == 4 :
                    case_n3 = "A"

        print("|   ["+case_n0+"]-+-["+case_n1+"]-+-["+case_n2+"]-+-["+case_n3+"]   |")
        
        
    print("|       |     |             |")
    print("|        -["+case_0+"]-              |")
    print("_____________________________")


print_board(10)


# case_n0 = str(9-i)
# case_n1 = str(10-i)
# case_n2 = str(11-i)
# case_n3 = str(12-i)
