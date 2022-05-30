#Law of Cosine Program
#Imported Libraries
import math #allows this program to use arccos and cosine operations. As well as converting answers from radian to degrees
#(Additional Info on Library) https://www.studytonight.com/post/trigonometric-function-in-python
import re #Imports regular expression commands to track specific inputs
#(Additional Info on Library) https://www.w3schools.com/python/python_regex.asp 
#Functions
def SSS():
    Sa = input("Enter First Side Value(a):") #Enter all values for sides
    Sb = input("Enter Second Side Value(b):")
    Sc = input("Enter Third Side Value(c):")
    Sa_Test = re.match("[0-9.]", Sa) #Checks if the input includes any set of numbers and or periods
    Sb_Test = re.match("[0-9.]", Sb)
    Sc_Test = re.match("[0-9.]", Sc)
    if Sa_Test and Sb_Test and Sc_Test: #If each input is an integer or a decimal, continue the program, else new inputs will be requested
        S_a = float(Sa) #Convert values into decimals
        S_b = float(Sb)
        S_c = float(Sc)
        CosA = ((S_a**2) - (S_b**2 + S_c**2))/(-2*S_b*S_c) #Performs Law of Cosine Equation before last step
        if CosA < 1: #Arc cosine value cannot be greater than 1 (Trig Rule)
            Cosine = math.acos(CosA) #(Last Step)Takes the result of equation and finds the arccos of answer
            Angle = math.degrees(Cosine) #Converts answer into degrees
            print(Angle)
        elif CosA > -1: #Arc cosine value cannot be less than -1 (Trig Rule)
            Cosine = math.acos(CosA) #(Last Step)Takes the result of equation and finds the arccos of answer
            Angle = math.degrees(Cosine) #Converts answer into degrees
            print(Angle)
        else:
            print("Domain Error")
            Format_Menu()
    else:
        print("Invalid Values")
        print("Make sure you input integers or decimals(Numbers)")
        SSS()
def SAS():
    SSb = input("Enter First Side Value(b):") #Enters side values of triangle
    SSc = input("Enter Second Side Value(c):")
    SSA = input("Enter the angle(degrees) in between the sides(CosA):") #Enter the angle between the two sides
    SSb_Test = re.match("[0-9.]", SSb) ##Checks if the input includes any set of numbers and or periods
    SSc_Test = re.match("[0-9.]", SSc)
    SSA_Test = re.match("[0-9.]", SSA)
    if SSb_Test and SSc_Test and SSA_Test: #If each input is an integer or a decimal, continue the program, else new inputs will be requested
        SS_b = float(SSb)#Converts input into decimals
        SS_c = float(SSc)
        SS_A = float(SSA)
        Radian_Conversion = (math.pi/180) #Finding the cosine of any amount of degrees is converted to radians in python. 
        #To counteract this, the degree input must be converted to radians before finding the cosine of it.
        #This will show the answer in degree mode.
        a = ((SS_b**2 + SS_c**2) - (2*SS_b*SS_c*(math.cos((SS_A)*Radian_Conversion))))**(1/2) #Performs Law of Cosine equation based off input
        print(a)
    else:
        print("Invalid Values")
        print("Make sure you input integers or decimals(Numbers)")
        SAS()
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
    try: 
        Format_Input == Input_Selection[0,1,2,3]
    except:
        print("Invalid Input")
        Format_Menu()
#Ask user if they are using SSS or SAS(Beginning of program)
Format_Menu()

