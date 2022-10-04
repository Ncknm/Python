# Homework 2


# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


print("\nЗадача 1.")
number = (input('Введите вещественное число: '))
total = 0
for i in number:
    if i != '.':
        total += int(i)
print(total)


# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


print("\nЗадача 2.")
n = int(input('Введите число N: '))
n_list = []
num = 1
for i in range(1, n + 1):
    n_list.append(num * i)
    num *= i
print(n_list)


# Задача 3. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.


print("\nЗадача 3.")
from math import *
n_list, total, n = [], 0, int(input('Введите число N: '))
for i in range(1, n + 1):
    n_list.append(round(float(((1 + 1 / i) ** i))))
    total = total + round(float(((1 + 1 / i) ** i)))
print(f'{n_list} -> {total}')


# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.


print("\nЗадача 4.")
path = 'file.txt'
data = open(path, 'r')
list_pos = []
for line in data:
    list_pos.append(int(line))
data.close()

list_numbers = []
n = int(input('Введите число N: '))
for i in range(-n, n + 1):
    list_numbers.append(i)
print(list_numbers)
total = 1
for pos in list_pos:
    if pos < len(list_numbers):
        total *= list_numbers[pos]
print(total)


# Задача 5. Реализуйте алгоритм перемешивания списка.


import random
print("\nЗадача 5 (методом Shuffle).")
list_shuffle = [1, 2, 4, 6, 7, 8, 'asd', 'asd']
print(f'Несортированный список:   {list_shuffle}')
random.shuffle(list_shuffle)
print(f'Сортированный список:   {list_shuffle}\n')


import random
print("\nЗадача 5 (методом замены элементов).")
def new_list(list_shuffle):
    list = list_shuffle[:]
    list_len = len(list)
    for i in range(list_len):
        index_random = random.randint(0, list_len - 1)
        temp = list[i]
        list[i] = list[index_random]
        list[index_random] = temp
    return list
list = [1, 2, 4, 6, 7, 8, 'asd', 'asd']
sort_list = new_list(list)
print("first list: ")
print(list)
print("second list: ")
print(sort_list)
