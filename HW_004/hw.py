# Homework 3
from random import randint
import itertools
import math
import numbers
import re

# Задача 1. Вычислить число c заданной точностью d.


print("\n[Задача 1.]")
d = int(input("Введите число для заданной точности числа: "))
print(f'Число Пи с заданной точностью {d}: {round(math.pi, d)}.')


# Задача 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


print("\n[Задача 2.]")
def simple_numbers(number):
    simple_num = 2
    number_list = []
    while simple_num <= number:
        if number % simple_num == 0:
            number_list.append(simple_num)
            number //= simple_num
            simple_num = 2
        else:
            simple_num += 1
    return number_list


print(f'Простые множители натурального числа: {simple_numbers(int(input("Введите натуральное число: ")))}')


# Задача 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


print("\n[Задача 3.]")
num_list = [1,2,3,3,3,4,5,6,6,7,8,9,9,10]
new_list = []
for i in num_list:
    total = 0
    for j in num_list:
        if i == j:
            total += 1
    if total == 1:
        new_list.append(i)
print(f'Последовательность: {num_list}.')
print(f'Неповторяющиеся числа в последовательности: {new_list}.')


# Задача 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.


print("\n[Задача 4.]")
k = randint(1, 4)
def get_numbers(k):
    numb = [randint(1, 10) for i in range(k + 1)]
    return numb

def create_polynom(k, numb):
    var = ['*x^'] * (k - 1) + ['*x']
    poly = [[a, b, c] for a, b, c in itertools.zip_longest(numb, var, range(k, 1, -1), fillvalue=' ') if a != 0]
    for x in poly:
        x.append('+')
    poly = list(itertools.chain(*poly))
    poly[-1] = '= 0'
    return ''.join(map(str, poly)).replace(' 1*x', 'x')

numbers = get_numbers(k)
polynom_1 = create_polynom(k, numbers)
print(f'Многочлен равен: {polynom_1}')

with open('polynomial_1.txt', 'w') as data:
    data.write(polynom_1)

numbers = get_numbers(k)
polynom_2 = create_polynom(k, numbers)
with open('polynomial_2.txt', 'w') as data:
    data.write(polynom_2)


# Задача 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


print("\n[Задача 5.]")
file1 = 'polynomial_1.txt'
file2 = 'polynomial_2.txt'
file_total = 'polynomial_total.txt'

# Получение данных из файла
def read_polynom(file):
    with open(str(file), 'r') as data:
        poly = data.read()
    return poly

# Получение списка кортежей каждого (<коэффициент>, <степень>)
def convert_pol(pol):
    poly = pol.replace('= 0', '')
    poly = re.sub("[*|^| ]", " ", poly).split('+')
    poly = [char.split(' ') for char in poly]
    poly = [[x for x in list if x] for list in poly]
    for i in poly:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    poly = [tuple(int(x) for x in j if x != 'x') for j in poly]
    return poly

# Получение списка кортежей суммы (<коэф1 + коэф2>, <степень>)
def decompose_pols(poly_1, poly_2):   
    x = [0] * (max(poly_1[0][1], poly_2[0][1] + 1))
    for i in poly_1 + poly_2:        
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key = lambda r: r[1], reverse = True)
    return res

# Составление итогового многочлена
def get_sum_pol(pol):
    var = ['*x^'] * len(pol)
    numbers = [x[0] for x in pol]
    degrees = [x[1] for x in pol]
    new_poly = [[str(a), str(b), str(c)] for a, b, c in (zip(numbers, var, degrees))]
    for x in new_poly:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1': 
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    new_poly = list(itertools.chain(*new_poly))
    new_poly[-1] = ' = 0'
    return "".join(map(str, new_poly))

def write_to_file(file, pol):
    with open(file, 'w') as data:
        data.write(pol)

polynom_1 = read_polynom(file1)
polynom_2 = read_polynom(file2)
pol_1 = convert_pol(polynom_1)
pol_2 = convert_pol(polynom_2)

pol_sum = get_sum_pol(decompose_pols(pol_1, pol_2))
write_to_file(file_total, pol_sum)

print(f"Первый многочлен: {polynom_1}")
print(f"Второй многочлен: {polynom_2}")
print(f"Сумма многочленов: {pol_sum}")