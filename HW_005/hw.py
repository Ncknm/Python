# Homework 5
import random


# Задача 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


print("\n[Задача 1.]")
line = 'Напишите программу абвгдейку, удаляющую из текста все слова, содержащие ""абв"".'
print(f"Исходный текст: {line}")
words = line.split(' ')
fragment = 'абв'
new_words = []
for word in words:
    if fragment not in word:
        new_words.append(word)
new_words = ' '.join(new_words)
print(f"Исправленный текст: {new_words}.")


# Задача 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?


print("\n[Задача 2.]")
first_user = random.randint(1, 2)
if first_user == 1:
    second_user = 2
elif first_user == 2:
    second_user = 1

candies = 2021
print(f"Первым ходит игрок №{first_user}!")
while candies > 0:
    print(f"Осталось конфет: {candies}.")
    number = int(input(f'Игрок №{first_user}, сколько конфет заберете? : '))
    while number < 1 or number > 28:
        number = int(input('Можно забрать от 1 до 28 конфет! Сколько конфет заберёте? '))
    candies -= number
    if candies < 1:
        print(f'Победил игрок №{first_user}!')
        break
    print(f"Осталось конфет: {candies}.")
    number = int(input(f'Игрок №{second_user}, сколько конфет заберете? : '))
    while number < 0 or number > 28:
        number = int(input('Можно забрать от 1 до 28 конфет! Сколько конфет заберёте? '))
    candies -= number
    if candies < 1:
        print(f'Победил игрок №{second_user}!')
        break


# Задача 2.а Добавьте игру против бота


print("\n[Задача 2.а]")
candies = 2021
comp = 0
motion = random.randint(1, 2)
if motion == 1:
    print("Первым ходит игрок!")
    while candies > 0:
        print(f"Осталось конфет: {candies}.")
        number = int(input('Сколько конфет заберете? '))
        while number < 0 or number > 28:
            number = int(input('Не жульничайте! Нужно забрать от 1 до 28 конфет! : '))
        candies -= number
        if candies<1:
            print('Поздравляем, Вы победили!')
            break
        print(f"Осталось конфет: {candies}.")
        comp = random.randint(1, 28)
        print(f"Компьютер забрал конфет: {comp}.")
        candies = candies - comp
        if candies < 1:
            print('К сожалению, Вы проиграли!')
            break
else:
    print("Первым ходит компьютер!")
    while candies > 0:
        print(f"Осталось конфет: {candies}.")
        comp = random.randint(1, 28)
        print(f"Компьютер забрал конфет: {comp}.")
        candies = candies - comp
        if candies < 1:
            print('К сожалению, Вы проиграли!')
            break        
        print(f"Осталось конфет: {candies}.")
        number = int(input('Сколько конфет заберете? '))
        while number < 0 or number > 28:
            number = int(input('Можно забрать от 1 до 28 конфет! Сколько конфет заберёте? '))
        candies -= number
        if candies < 1:
            print('Поздравляем, Вы победили!')
            break


# Задача 2.б Подумайте как наделить бота ""интеллектом""


print("\n[Задача 2.б]")
candies = 2021
comp = 0
motion = random.randint(1, 2)
if motion == 1:
    print("Первым ходит игрок!")
    while candies > 0:
        print(f"Осталось конфет: {candies}!")
        number = int(input('Сколько конфет заберете? '))
        while number < 0 or number > 28:
            number = int(input('Можно забрать от 1 до 28 конфет! Сколько конфет заберёте? '))
        candies -= number
        if candies<1:
            print('Поздравляем, Вы победили!')
            break
        print(f"Осталось конфет: {candies}!")
        if candies <= 85 and candies >= 58:
            comp = candies - 29 * 2
        elif candies <= 57 and candies >= 30:
            comp = candies - 29
        elif candies < 29:
            comp = candies
        else:
            comp = random.randint(1, 28)
        print(f"Компьютер забрал конфет: {comp}!")
        candies = candies - comp
        if candies < 1:
            print('К сожалению, Вы проиграли!')
            break   
else:
    print("Первым ходит компьютер!")
    while candies > 0:
        print(f"Осталось конфет: {candies}!")
        if candies <= 85 and candies >= 58:
            comp = candies - 29 * 2
        elif candies <= 57 and candies >= 30:
            comp = candies - 29
        elif candies < 29:
            comp = candies
        else:
            comp = random.randint(1, 28)
        print(f"Компьютер забрал конфет: {comp}!")
        candies = candies - comp
        if candies < 1:
            print('К сожалению, Вы проиграли!')
            break        
        print(f"Осталось конфет: {candies}!")
        number = int(input('Сколько конфет заберете? '))
        while number < 0 or number > 28:
            number = int(input('Можно забрать от 1 до 28 конфет! Сколько конфет заберёте? '))
        candies -= number
        if candies < 1:
            print('Поздравляем, Вы победили!')
            break


# Задача 3. Создайте программу для игры в ""Крестики-нолики"".


print("\n[Задача 3.]")
playing_area = list(range(1, 10))
winning_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (7, 5, 3), (9, 5, 1), (7, 4, 1), (8, 5, 2), (9, 6, 3)]

def create_playing_area ():
    print('-' * 15)
    for i in range(3):
        print('|', playing_area[0 + i*3], '|', playing_area[1 + i*3], '|', playing_area[2 + i*3], '|')
    print('-' * 15)

def take_enter(step):
    while True:
        meaning = input('Выберите поле: '+ step + '?: ')
        if not (meaning in '123456789'):
            print('Попробуйте снова.')
            continue
        meaning = int(meaning)
        if str(playing_area[meaning - 1]) in 'XO':
            print('Поле занято.')
            continue
        playing_area[meaning - 1] = step
        break

def check_winning_combinations ():
    for each in winning_combinations:
        if (playing_area[each[0] - 1] == playing_area[each[1] - 1] == playing_area[each[2] - 1]):
            return playing_area[each[1] - 1]
    else:
        return False

def main():
    total = 0
    while True:
        create_playing_area()
        if total % 2 == 0:
            take_enter('X')
        else:
            take_enter('O')
        if total > 3:
            winner = check_winning_combinations()
            if winner:
                create_playing_area()
                print(winner + ' победил!')
                break
        total += 1
        if total > 8:
            create_playing_area()
            print('Ничья.')
            break
main()


# Задача 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


print("\n[Задача 4.]")
with open('file_encode.txt', 'w') as data:
    data.write('222222225555777786666uuuuuuuuuuuuuuuuuuuuuuwwwwwww')

with open('file_encode.txt', 'r') as data:
    string = data.readline()

def rle_encode(decoded_string):
    encoded_string = ''
    count = 1
    char = decoded_string[0]
    for i in range(1, len(decoded_string)):
        if decoded_string[i] == char:
            count += 1
        else:
            encoded_string = encoded_string + str(count) + char
            char = decoded_string[i]
            count = 1
            encoded_string = encoded_string + str(count) + char
    return encoded_string

def rle_decode(encoded_string):
    decoded_string = ''
    char_amount = ''
    for i in range(len(encoded_string)):
        if encoded_string[i].isdigit():
            char_amount += encoded_string[i]
        else:
            decoded_string += encoded_string[i] * int(char_amount)
        char_amount = ''
    print(decoded_string)

    return decoded_string

with open('file_encode.txt', 'r') as file:
    decoded_string = file.read()

with open('file_decode.txt', 'w') as file:
    encoded_string = rle_encode(decoded_string)
    file.write(encoded_string)

print('Decoded string: \t' + decoded_string)
print('Encoded string: \t' + rle_encode(decoded_string))
print(f'Compress ratio: \t{round(len(decoded_string) / len(encoded_string), 1)}')