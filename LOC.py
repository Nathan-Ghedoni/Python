#Law of Cosine Program
#Imported Libraries
import math #allows this program to use arccos and cosine operations. As well as converting answers from radian to degrees
#Functions
def SSS():
    Sa = input("Enter First Side Value(a):") #Enter all values for sides
    Sb = input("Enter Second Side Value(b):")
    Sc = input("Enter Third Side Value(c):")
    S_a = float(Sa) #Convert values into decimals
    S_b = float(Sb)
    S_c = float(Sc)
    CosA = ((S_a**2) - (S_b**2 + S_c**2))/(-2*S_b*S_c) #Performs Law of Cosine Equation before last step
    if CosA < 1:    
        Cosine = math.acos(CosA) #(Last Step)Takes the result of equation and finds the arccos of answer
        Angle = math.degrees(Cosine) #Converts answer into degrees
        print(Angle)
    elif CosA > -1:
        Cosine = math.acos(CosA) #(Last Step)Takes the result of equation and finds the arccos of answer
        Angle = math.degrees(Cosine) #Converts answer into degrees
        print(Angle)
    else:
        print("Domain Error")
        Format_Menu()
def SAS():
    SSb = input("Enter First Side Value(b):") #Enters side values of triangle
    SSc = input("Enter Second Side Value(c):")
    SSA = input("Enter the angle(degrees) in between the sides(CosA):") #Enter the angle between the two sides
    SS_b = float(SSb)#Converts input into decimals
    SS_c = float(SSc)
    SS_A = float(SSA)
    SSS_A = math.degrees(SS_A)
    a = ((SS_b**2 + SS_c**2) - (2*SS_b*SS_c*math.cos(SSS_A)))**(1/2) #Performs Law of Cosine equation based off input
    print(a)
def Format_Menu():
    Format_Input = input("What data do you currently have?\n1.SSS\n2.SAS\nq.Quit Program\nEnter either 1,2, or q(Quit Program):")
    if Format_Input == "1":
        SSS()
        Format_Menu()
    if Format_Input == "2":
        SAS()
        Format_Menu()
    if Format_Input == "q":
        exit()
    #Values for Input
    SSS_1 = "1"
    SAS_2 = "2"
    Quit = "q"
    Enter = None
    Input_Selection = [SSS_1, SAS_2, Quit, Enter]
    try: Format_Input == Input_Selection[0,1,2,3]
    except:
        print("Invalid Input")
        Format_Menu()
#Ask user if they are using SSS or SAS(Beginning of program)
Format_Menu()

