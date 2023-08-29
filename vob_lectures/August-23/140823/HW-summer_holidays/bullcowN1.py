# -* coding: utf-8 -*-
# The numerical version of the game is usually played with 4 digits,
# but can also be played with 3 or any other number of digits.
# On a sheet of paper, the players each write a 4-digit secret number.
# The digits must be all different. Then in turn the players try 
# to guess their opponent's number who gives the number of matches.
# If the matching digits are in their right positions, they are "bulls", if in different positions, they are "cows".
#####-Example:#####
# Secret number - 4271
# Opponent's try - 1234
# Answer - a) 1 bull - the bull is "2"; b) 2 cows - the cows are "4" and "1".
# The first one to reveal the other's secret number wins the game. As the first player has a logical advantage, the game can be balanced over multiple games
# by alternating the right to go first, or over a single game by granting the second player
# an equal number of quesses, posibly resulting in a tie.
#&&&& The game may also be played by two teams of 2-3 players, with the team members 
#&&&& discussing their strategy before selecting a move.
#!!!!-Lower a solution of this game for two teams with one leader
#!!!!              who knows the SECRET NUMBER-!!!#
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
        print (number)
        print("You won after " , approaches,  " approaches!")
    if(bulls !=4):
        MainGame()
    
DetNumber()
MainGame()   