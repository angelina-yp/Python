# 1.1 Напишите и запустите программу.которая выводит строку "Hello world!"
print("Hello world!")
# 1.2.Напишите программу, которая на входе получает имя пользователя, cохраняет его в переменную user_name и выводит строку  "Hello {user_name}!"
user_name=input("Please, enter user name:")
print(f"Hello, {user_name}!")
# 1.3 Напишите программу, которая на входе получает 2 числа, производит с ними арифметическую операцию(на ваше усмотрение), и выводит “Результат = {результат}”.
number1 = int(input('Please, enter first number: '))
number2 = int(input('Please, enter second number: '))
print(f"Результат= {number1+number2}")
# print(f"Результат= {number1*number2}")
# print(f"Результат= {number1-number2}")
# number1 = int(input('Please, enter first number: '))
# number2 = int(input('Please, enter second number: '))
# print(f"Результат= {number1+number2}")
# print(f"Результат= {number1*number2}")
# print(f"Результат= {number1-number2}")
# # Напишите программу, чтобы вывести:
# # ** ** ** ** *
# # *           *
# # *           *
# # ** ** ** ** *
print("""** ** ** ** *
*           *
*           *
** ** ** ** *""")
# Задание 2.1
# Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран False, в противном случае True.
zdorov=int(input('Please, enter zdorov: '))
if zdorov <=0:
     print('False')
 else:
     print('True')

# Задание 2.2
# Напишите программу, которая проверяет является ли введенное число четным. Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”
 chislo=int(input('Please, enter chislo: '))
 if chislo%2:
     print('Нечетное')
 else:
     print('Четное')

# Задание 2.3
# Напишите программу, которая проверяет является ли год високосным. Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008) и не являются столетиями (500, 600). Однако, если год делится без остатка  на 400, он также считается високосным (1200, 2000)
# year=int(input('Please, enter year: '))
 if year%4 or year%100 or year%400:
     print('Не високосный')
 else:
     print('Високосный')
# Задание 2.4
# Напишите программу, которая печатает введенный текст заданное количество раз, построчно. Текст и количество повторений нужно ввести с помощью input()
# text=input('Please, enter text: ')
# i=1
# num=int(input('Please, enter num: '))
# while i<num:
#     i+=1
#     print(text)
# Задание 2.5.
# Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str), производит заданное арифметическое действие и печатает результат в формате: {num1} {operator) {num2) = {result}

# try:
#     num1 = int(input('Please, enter num1: '))
#     num2 = int(input('Please, enter num2: '))
# except ValueError as e:
#     print(f'No number: {e}')
#     sys.exit()
# operator = str(input('Enter operator -  \'/\', \'*\', \'%\', \'+\', \'-\': '))
# if operator not in '+-*/%':
#     print("No operator")
#     sys.exit()
# result = 0
# if num2 == 0 and operator == '/':
#     try:
#         result = num1 / num2
#     except ZeroDivisionError:
#         print('error/0')
#         sys.exit()
# elif operator == '*':
#     result = num1 * num2
# elif operator == '+':
#     result = num1 + num2
# elif operator == '-':
#     result = num1 - num2
# elif operator == '%':
#     result = num1 % num2
# else:
#     result = num1/num2
# print(f'{num1} {operator} {num2} = {result}')
