# Derek Ruggirello's game machine.

# Imports for additional functions
from random import randint
from tkinter import *
from tkinter import ttk
import random
import turtle

# Creates the initial box with a title (Game Menu)
main_box = Tk()
main_box.geometry("1000x600")
main_box.title("Game Menu")
Label(main_box, text="Choose a game!", font="arial 32").pack(fill=X)

# Function for madlib game asking for input and producing a short sentence.
def MadLib():
    dic1={"person":"", "place":"", "adjective":"", "noun":""}
    # Spellcheck is implemented in order to stop illegal characters.
    dic1["person"] = input("Enter a person:")
    dic1["person"] = spellcheck(dic1["person"])
    dic1["place"] = input("Enter a place:")
    dic1["place"] = spellcheck(dic1["place"])
    dic1["adjective"] = input("Enter an adjective:")
    dic1["adjective"] = spellcheck(dic1["adjective"])
    dic1["noun"] = input("Enter a noun:")
    dic1["noun"] = spellcheck(dic1["noun"])

    print("It looks like %s is going to %s in order to buy a %s %s." % (dic1["person"], dic1["place"], dic1["adjective"], dic1["noun"]))

# Spellcheck function in order to stop all illegal characters
def spellcheck(word):
    if '$' in word:
        word = input("Invalid character please retype input: ")
        word = spellcheck(word)
        return word
    if '%' in word:
        word = input("Invalid character please retype input: ")
        word = spellcheck(word)
        return word
    if '^' in word:
        word = input("Invalid character please retype input: ")
        word = spellcheck(word)
        return word
    if '.' in word:
        word = input("Invalid character please retype input: ")
        word = spellcheck(word)
        return word
    if '&' in word:
        word = input("Invalid character please retype input: ")
        word = spellcheck(word)
        return word
    if '0' in word:
        word = input("Invalid character please retype input: ")
        word = spellcheck(word)
        return word
    if '1' in word:
        word = input("Invalid character please retype input: ")
        word = spellcheck(word)
        return word
    if '2' in word:
        word = input("Invalid character please retype input: ")
        word = spellcheck(word)
        return word
    if '3' in word:
        word = input("Invalid character please retype input: ")
        word = spellcheck(word)
        return word
    if '4' in word:
        word = input("Invalid character please retype input: ")
        word = spellcheck(word)
        return word
    if '5' in word:
        word = input("Invalid character please retype input: ")
        word = spellcheck(word)
        return word
    if '6' in word:
        word = input("Invalid character please retype input: ")
        word = spellcheck(word)
        return word
    if '7' in word:
        word = input("Invalid character please retype input: ")
        word = spellcheck(word)
        return word
    if '8' in word:
        word = input("Invalid character please retype input: ")
        word = spellcheck(word)
        return word
    if '9' in word:
        word = input("Invalid character please retype input: ")
        word = spellcheck(word)
        return word
    else:
        return word



# Polygon game that creates a random sided polygon with turtle
def RandPol():
    sides = random.randint(1,12)
    colors = ["green","purple","blue","brown","black","yellow"]
    rand_index = random.randint(0,len(colors)-1)
    turk = turtle.Turtle()
    turk.color(colors[rand_index])
    for i in range(sides):
        turk.forward(80)
        turk.right(360/sides)
    turk.screen.mainloop()

# Polygon game that asks for user input on the polygon sides, length, and color
def UserPol():
    sides = int(input("Enter the number of sides: "))
    length = int(input("Enter the size of each side: "))
    color = input("Enter the color of the polygon: ")
    turk = turtle.Turtle()
    turk.color(color)
    for i in range(sides):
        turk.forward(length)
        turk.right(360/sides)
    turk.screen.mainloop()

# Simple quit function when done with program
def Quit_Function():
    quit()

# Buttons for each GUI object
Button(main_box, text="Madlib", font='arial 12', command=MadLib, bg="light blue").place(x=100, y=200)
Button(main_box, text="Random Polygon", font='arial 12', command=RandPol, bg="light blue").place(x=700, y=200)
Button(main_box, text="Input Polygon", font='arial 12', command=UserPol, bg="light blue").place(x=100, y=400)
Button(main_box, text="Quit", font='arial 12', command=Quit_Function, bg="light blue").place(x=700, y=400)

main_box.mainloop()