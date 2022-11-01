# Homework 6
import random

# Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.


print("\n[Задача 1.]")
def sum_odd_index(lst):
    s = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            s += lst[i]
    print(f"Сумма чисел на нечётных позициях: {s}")

lst = list(map(int, input("Введите числа через пробел: ").split()))
sum_odd_index(lst)


# Задача 2. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


print("\n[Задача 2.]")
lst = list(map(float, input("Введите числа через пробел: ").split()))
new_lst = [round(i%1,2) for i in lst if i%1 != 0]
print(f'Разница между максимальным и минимальным числами: {max(new_lst) - min(new_lst)}')


# Задача 3. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


print("\n[Задача 3.]")
my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
    этого абв текста все вабвс слова, содерабващие содержащие "абв"'

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

print(f"Исходный текст: {my_text}")
my_text = del_some_words(my_text)
print(f"Исправленный текст: {my_text}.")


# Задача 4. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


print("\n[Задача 4.]")
list3 = [random.randint(0,10) for i in range(random.randint(5,10))]
result_list = list(filter(lambda a: list3.count(a) == 1, list3))
print(f'Последовательность: {list3}.')
print(f'Неповторяющиеся числа в последовательности: {result_list}.')