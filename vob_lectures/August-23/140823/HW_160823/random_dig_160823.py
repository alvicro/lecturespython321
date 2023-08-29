# * * * H O M E  W O R K (14.08.23) * * * 
#Домашнее задание: используя только random.randint() или random.choice()
#реализовать (придумать) алгоритм получения последовательности неповторяющихся цифр
#случайных чисел
import random
numbers = [0,1,2,3,4,5,6,7,8,9]
detres = []
n = int(input("Input a number of random digits: "))
for i in range (n):
    x = random.choice(numbers)
    detres.append(str(x))
print(detres)
random_dig = ''.join(detres)
print("With the help of random.choice we determined random number - ",random_dig)
