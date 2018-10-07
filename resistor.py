#Made by DaisukeDany

#imports
import os

#Methods
def CalculateResistor():
    FinalValue = ""
    os.system('cls')
    print("Write the first color")
    print(" -Black -Brown -Red -Orange -Yellow -Green -Blue -Purple -Gray -White")
    Color1 = input().lower()
    print("Write the next color")
    Color2 = input().lower()
    print("Write the last color")
    Color3 = input().lower()

    #Get value by first Color
    if Color1 == "black":
        FinalValue = FinalValue + "0"
    elif Color1 == "brown":
        FinalValue = FinalValue + "1"
    elif Color1 == "red":
        FinalValue = FinalValue + "2"
    elif Color1 == "orange":
        FinalValue = FinalValue + "3"
    elif Color1 == "yellow":
        FinalValue = FinalValue + "4"
    elif Color1 == "green":
        FinalValue = FinalValue + "5"
    elif Color1 == "blue":
        FinalValue = FinalValue + "6"
    elif Color1 == "purple":
        FinalValue = FinalValue + "7"
    elif Color1 == "gray":
        FinalValue = FinalValue + "8"
    elif Color1 == "white":
        FinalValue = FinalValue + "9"
    else:
        print("Error: Are you sure you typed a color?")
        input()

    #Get second value by Second color
    if Color2 == "black":
        FinalValue = FinalValue + "0"
    elif Color2 == "brown":
        FinalValue = FinalValue + "1"
    elif Color2 == "red":
        FinalValue = FinalValue + "2"
    elif Color2 == "orange":
        FinalValue = FinalValue + "3"
    elif Color2 == "yellow":
        FinalValue = FinalValue + "4"
    elif Color2 == "green":
        FinalValue = FinalValue + "5"
    elif Color2 == "blue":
        FinalValue = FinalValue + "6"
    elif Color2 == "purple":
        FinalValue = FinalValue + "7"
    elif Color2 == "gray":
        FinalValue = FinalValue + "8"
    elif Color2 == "white":
        FinalValue = FinalValue + "9"
    else:
        print("Error: Are you sure you typed a color?")
        input()

    #Third value
    if Color3 == "black":
        FinalValue = FinalValue + ""
    elif Color3 == "brown":
        FinalValue = FinalValue + "0"
    elif Color3 == "red":
        FinalValue = FinalValue + "00"
    elif Color3 == "orange":
        FinalValue = FinalValue + "000"
    elif Color3 == "yellow":
        FinalValue = FinalValue + "0000"
    elif Color3 == "green":
        FinalValue = FinalValue + "00000"
    elif Color3 == "blue":
        FinalValue = FinalValue + "000000"
    elif Color3 == "purple":
        FinalValue = FinalValue + "0000000"
    elif Color3 == "gray":
        FinalValue = FinalValue + "00000000"
    elif Color3 == "white":
        FinalValue = FinalValue + "000000000"
    else:
        print("Error: Are you sure you typed a color?")
        input()

    os.system('cls')
    print("Values inserted:\n%s - %s - %s\nCalculation:\n%s" % (Color1, Color2, Color3, FinalValue))
    input()

#First Option must be empty
option = ""


while option != 2:
    os.system('cls')
    #Title
    print("Python Resistor Calculator")

    print("What you want to do?")
    print("1.-Calculate a the value of a Resistor\n2.-Exit")
    option = input()
    if option == "1":
        CalculateResistor()
    else:
        print("Exited")
        break
