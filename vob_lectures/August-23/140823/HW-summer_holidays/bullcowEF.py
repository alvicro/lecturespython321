# -* coding: utf-8 -*-
# # # EN # # # ! ! ! EN ! ! ! & & & EN & & &
# The numerical version of the game is usually played with 4 digits,
# but can also be played with M number (<= 9) of digits.
# The digits must be all different. Then in turn the players try 
# to guess their opponent's number who gives the number of matches.
# If the matching digits are in their right positions, they are "bulls", 
# if in different positions, they are "cows".
#&&&& The game may also be played by two teams of 3 / N players, with the team members 
#&&&& discussing their strategy before selecting a move.
# # # FR # # # ! ! ! FR ! ! ! & & & FR & & &
#!!!!-Abaissez une solution de ce jeu pour deux equipes avec un leader 
# (Generateur de nombres aleatoires) qui connait le NUMERO SECRET-!!!!#
#!!!!-Ceulement a la fin du jeu, les deux equipes apprendront enfin un numero secret
# genere aleatoirement-!!!!#.
import random
number = []
approaches = 0
def DetNumber():
    for i in range(4):
        x = random.randrange(0, 9)
        number.append(x)
    if len(number) > len(set(number)):
        number.clear()
        DetNumber()
        
def MainGame():
    global approaches
    approaches += 1
    cows = 0
    bulls = 0
    choice = input("Please enter a 4 digit number ")
    guess = []
    for i in range (4):
        guess.append(int(choice[i]))
    for i in range (4):
        for j in range (4):
            if(guess[i] == number[j]):
                cows +=1
    for x in range (4):
        if guess[x] == number[x]:
            bulls +=1
    cows = cows - bulls
    print("Bulls: ", bulls)
    print("Cows: ", cows)
    if (bulls == 4):
        print(number)
        print("You won after " , approaches,  " approaches!")
    if(bulls !=4):
        MainGame()
    
DetNumber()
MainGame()
    
                     
    
    