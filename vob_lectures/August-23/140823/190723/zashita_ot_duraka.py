Спросить_опять = True

while Спросить_опять:
    size = input('Какого размера поле? 5x6\n')
    Спросить_опять = 'x' not in size
    if not Спросить_опять:   # икс присутствует - проверяем числа
        xy = size.split('x')
        print(xy)# функция сплит разрежет строку на список из строк до икса и после икса
        Спросить_опять = len (xy) != 2 or not xy[0].isdigit() or not xy[1].isdigit()

x = int(xy[0])
y = int(xy[1])
top_bottom = 'O' * y + '\n'
middle = ('O' + (' ' * (y - 1 - 1)) + 'O' + '\n') * (x - 1 -1)
print(top_bottom + middle + top_bottom)
