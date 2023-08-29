# Списки (list) и кортежи (tuple)

colors = ['red', 'green', 'blue']  # список, похож на массив в js
rainbow = ('red', 'orange', 'yellow', 'green', 'marine', 'blue', 'violet')

# чтение: []
second_color = colors[1]
last_color = rainbow[-1]   # отрицательные значения - нумерация с конца

# Упражнение: какие цвета получились? Напечатайте

# запись: []
colors[1] = 'yellow'   # превратили цвета пикселя в цвета принтера
try:
    rainbow[4] = 'light-blue'
except TypeError as te:  # создание переменной в процессе перехвата исключения
    print(te)

# удаление:
del colors[1]   # оператор удаления работает не только для частей коллекции, но и для наших переменных
print(colors)

a = 8
del a
try:
    print(a)
except NameError as ne:
    print(ne)

try:
    del rainbow[1]
except TypeError as te:
    print(te)

# Так ли надёжен кортеж?

cortej = (
    ['Volga', 'black'],
    ['Niva', 'green']
)

cortej[0][1] = 'red'
del(cortej[1][1])
print(cortej)

# Вывод: только верхний уровень кортежа защищен от записи
# как защитить? Сделать кортежи (tuple) внутри
cortej = (
    ('Volga', 'black'),
    ('Niva', 'green')
)

# Пополнение списка
colors.append('white')  # родная функция приклеивания в конец. Работает быстро!
colors += ['black']     # возможность сложить два списка
colors = ['purple'] + colors
colors += 'lilac'
print(colors)

# Фишка кортежа и висящая запятая

# Пустой кортеж

c = ()
print(type(c), c)

# Кортеж из 2 элементов (пара)

coords = (37, 53)
print(type(coords), coords)

# Кортеж из одного элемента

# u = (8, )
u = (8, )
print(type(u), u)

# Следствие - допустима висящая запятая

razdvatri = [1, 2, 3, ]

# Поддерживается срез (slice)

# Цикл перебирает список по элементам

for c in coords:
    print('coord: ', c)

# Строго не рекомендуется (почти запрещается) модифицировать список в процессе перебора

# 1. Пример бесконечного цикла. Осторожно: в какой-нибудь версии это могут заблокировать
coords = [37, 53]

#for c in coords:
#    coords.append('b')
#    print(c)

# 2. Пример "неожиданного" поведения: напечатан оказывается именно удалённый элемент
coords = [37, 53]

for c in coords:  # ПРОСТО первый стал нулевым и цикл закончился раньше времени
    del coords[0]
    print(c)

# проверка "вхождения" элемента в список и кортеж

print('53 in coords', 53 in coords)

# 1) Сложить два списка.
# 2) Сравнить два списка циклом (for "почти" не подойдёт).
# 3) Создать список букв слова "кенгуру".
# 4) Создать список разных букв строки, введённой с клавиатуры.
####### * 1 * #######
fourfivesix = [4, 5, 6, ]
summary = razdvatri + fourfivesix
print (summary)

####### * 2 * #######
first = ['f', 'i', 'r', 's', 't', ]
second = ['s', 'e', 'c', 'o', 'n', 'd', ]
third = [] 

for i in first:  
    if i in second:  
        third.append(i) 
print(third)

####### * 3 * #######
kenguru = ['k', 'e', 'n', 'g', 'u', 'r', 'u', ]
del(kenguru[4])
print (kenguru)

###### * 4 * #######
letters = [1, 2, 3, 4, 5, ]
letters[0] = input ('H')
letters[1] = input ('E')
letters[2] = input ('L')
letters[3] = input ('L')
letters[4] = input ('O')
print (letters)









