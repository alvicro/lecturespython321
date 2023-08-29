#1) Выяснить, какие номера символов не совпадают в двух введенных строках (вернуть список)
#2) Выяснить, сколько символов второй строки встречается в первой
# * * * H O M E  W O R K * * * - 15.08.23 (only for digits)
letter_list1 = []
line1 = []
line2 = []
j = 0
kk = 0
for i in range(1,4):    
    letter1 = input("Input letter for line1: ")
    letter1 = str(letter1)
    print(letter1)
    line1.insert(i,letter1)    
    letter2 = input("Input letter for line2: ")
    letter2 = str(letter2)
    print(letter2)
    line2.insert(i,letter2)
print("Finally we formed the list 'line1': ", line1)
print("Enfin nous avons forme une liste 'line2': ", line2)
for k in line1:
    if k in line2:
        letter_list1.append(k)
        j = j + 1
        kk = int(k) - 1
        print ("Adding letters to letter_list1 (j) - sum of these numbers: ", j ,
               "Number of letter in list1(kk): ", kk)
print ("FINAL list 'letter_list1' with letters from 'line1', which are situated in 'line2': ")
print (letter_list1)