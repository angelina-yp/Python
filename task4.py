# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
# def square(storona):
#     return {tuple(storona, storona, storona, storona)}
#
# print(2)
# print(sum(my_kvadrat))
# print(storona**2)
# import math
# num = 2
# sqrt = math.sqrt(num)
# print(storona*math.sqrt(num))
# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer

# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа
# my_list=[20, -3, 15, 2, -1, -21]
# positive_num = list(filter(lambda x: (x>=0),my_list))
# print(positive_num)
# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# from functools import reduce
# my_list = [20, -3, 15, 2, -1, -21]
# ym = reduce((lambda x, y: x * y), my_list)
# print(ym)
# # 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
# def timemometr(func):
#     from time import time
#     def wrapper(*args):
#         start_time = time()
#         value = func(*args)
#         end_time = time()
#         print(f'Время выполнения функции {end_time-start_time} сек.')
#         return value
#     return wrapper
# @timemometr
# def summa():
#     from time import sleep
#     sleep(2)
#     return 11
# print(summa())

# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      # Примените эти функции в качестве методов в другом файле.
# from my_calc import *
# print(sum(1,4))
# print(raz(6,4))
# print(ym(1,4))
# print(delen(8,4))