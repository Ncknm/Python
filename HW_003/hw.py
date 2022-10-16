# Homework 3
import math
from pickletools import string1

# Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.


print("\nЗадача 1.")
list_numbers = [2, 3, 5, 9, 3]
sum = 0
print(f'Ваш массив: {list_numbers}')
for i in range(len(list_numbers)):
    if i % 2 != 0:
        sum += list_numbers[i]
print(f'Сумма чисел на нечётных позициях: {sum}.')


# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.


print("\nЗадача 2.")
def product_pairs(list):
    product_list = []
    for i in range(1, math.ceil((len(list) / 2) + 1)):
        product_list.append(list[i - 1] * list[-i])
    return product_list
list_numbers = [2, 3, 4, 5, 6]
print(f'Ваш массив: {list_numbers}')
print(f'Произведение пар: {product_pairs(list_numbers)}')


# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


print("\nЗадача 3.")
def min_max(list):
    min, max = list[0], 0
    for i in range(1, len(list)):
        if list[i] == 0:
            min, max = min, max
        elif list[i] > max:
            max = list[i]
        elif list[i] < min:
            min = list[i]
    print(f'Минимальное число: {min}')
    print(f'Максимальное число: {max}')
    return max - min
def fract_list(list):
    fract_list = []
    for i in range(0, len(list)):
        fract_list.append(round(list[i] - math.floor(list[i]), 2))
    return fract_list
list_numbers = [1.1, 1.2, 3.1, 5, 10.01]
print(
    f'Разница между максимальным и минимальным числами: {min_max(fract_list(list_numbers))}')


# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.


print("\nЗадача 4.")
def binary(number):
    binary_number = ''
    while number > 0:
        binary_number = str(number % 2) + binary_number
        number = number // 2
    return binary_number
print(f'Ваше число в двоичной системе: {binary(int(input("Введите десятичное число: ")))}.')


# Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


print("\nЗадача 5.")


def fibonacci(number):
    fibo_numbers = []
    a, b = 1, 1
    for i in range(number - 1):
        fibo_numbers.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(number):
        fibo_numbers.insert(0, a)
        a, b = b, a - b
    return fibo_numbers


print(f'Список Фибоначчи: {fibonacci(int(input("Введите число: ")) + 1)}')
