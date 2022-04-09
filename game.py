#!/bin/python3
from ast import Break
from random import randint


def ComputerMugging():
    while True:
        playerChoice = input(WillSmith)
        if playerChoice == ("Wallet"):
            print ("Thanks Bud, good choice. *Walks away*")
            break
        elif playerChoice != ("Wallet"):
            print ("I didn't ask for", playerChoice + "!" " Show me your wallet!")        






#create a list of play options
t = ["Rock","Paper","Scissors","Gun"]

WillSmith = "Rock, Paper, Scissors?\nType your shit here: "

pandoraBox = False

while True:
    #set playerChoice to True
    playerChoice = input(WillSmith)
    if not playerChoice in t:
        print ("That didn't work! You could have typed Gun for all I care!")
        continue
       
    computer = t[randint(0,3 if pandoraBox else 2)]

    if playerChoice == computer:
        print("Tie!")

    elif computer == "Gun":
        print("Computer shows Gun and insists you choose wallet.")
        ComputerMugging()

    elif playerChoice == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", playerChoice)
        else:
            print("You win!", playerChoice, "smashes", computer)

    elif playerChoice == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", playerChoice)
        else:
            print("You win!", playerChoice, "covers", computer)

    elif playerChoice == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", playerChoice)
        else:
            print("You win!", playerChoice, "cut", computer)

    elif playerChoice == "Gun":
        print("Computer brought", computer, "to a gun fight")
        pandoraBox = True