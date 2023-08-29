# -* coding: utf-8 -*-
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
    
                     
    
    