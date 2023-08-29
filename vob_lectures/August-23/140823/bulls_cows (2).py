# Быки и коровы
# Загадывается последовательность (слово, число и т.д.) из N символов
# Пусть есть 4-значное число (загаданное вашей программой!)

# Игрок (человек) высказывает предположения
# и получает диагностику:
#    быки - буквы, стоящие на своих местах,
#    коровы - буквы (или цифры), присутствующие, но не на своём месте

# Посчитывается количество попыток
# Предлагается новая игра
# Важно: грамотная запись: 1 бык, 3 быка, 11 быков

# Упрощение: угадать 4-х значное число, сравнивая на равенство

import random

############ Функуция загадывания числа из неповторяющихся цифр ################

def zagadaika(alphebet='0123456789', word_len=4):  # ARGUMENTS?
    result = ''.join(random.sample(alphebet, word_len))
    #                 ['6', '2', '7', '9']
    # Домашнее задание: используя только random.randint() или random.choice()
    #   реализовать (придумать) алгоритм получения последовательности неповторяющихся цифр
    return result


def skolko_bykov(chislo, popitka):
    bulls = 0
    
    for i in range(len(chislo)):
        if chislo[i] == popitka[i]:
            bulls += 1
    return bulls


def skolko_korov(chislo, popitka):
    cows = 0
    for i in range(len(chislo)):
        if popitka[i] in chislo:
            cows += 1
    return cows


def main_game():
    chislo = zagadaika()
    print(chislo)
    bylo_popytok = 0
    popitka = ''
    while popitka != chislo:
        bylo_popytok += 1
        popitka = input('Введите 4-х значное число: ')
        if len(popitka) == len(chislo):
            print(skolko_bykov(chislo, popitka), ' быков')  # TODO: окончания!!!!
            print(skolko_korov(chislo, popitka), ' коров')  # TODO: окончания!!!!
    return bylo_popytok

    
otvet = 'Да'
while otvet == 'Да':
    print('Угадал за ', main_game(), ' попыток!')  # TODO: окончания!!!111
    otvet = input('Сыграем ещё? ')
