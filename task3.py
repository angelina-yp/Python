# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
my_list = ['a', 'b', [1, 2, 3], 'd']
print(my_list[2])
print(my_list[2][0])
print(my_list[2][1])
print(my_list[2][2])
3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
   - получите сумму всех чисел,

list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
sum = 0
for num in list_1:
    try:
        sum += num
    except TypeError:
        print(f"Элемент {num} не является числом")
print(f"Сумма чисел в списке: {sum}")
   - распечатайте все строки, где есть буква 'a'
list_2 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]

for item in list_2:
    if 'a' in str(item):
        print(item)
3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж

list = ['cat', 'dog', 'horse', 'cow']
print(list )
print(type(list ))
list_tuple = tuple(list)
print(list_tuple)
print(type(list_tuple))
3.4. Напишите программу, которая определяет, какая семья больше.
      1) Программа имеет два input() - например, family_1, family_2.

family_1 = tuple(input('Please, enter family_1: ').split(','))
family_2 = tuple(input('Please, enter family_1:: ').split(','))
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
a = len(family_1)
b = len(family_2)
if a == b:
    print("Equal")
elif a > b:
    print("family_1")
else:
    print("family_2")

3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
my_dictionary_film = {'title': 'name', 'director':1, 'year': 2023, 'budget': 4, 'main_actor': 132, 'slogan': 4}

print(my_dictionary_film)

#     - распечатайте только ключи
for key in my_dictionary_film.keys():
    print(key)

# #     - распечатайте только значения
for value in my_dictionary_film.values():
    print(value)

#     - распечатайте пары ключ - значение
for items in my_dictionary_film.items():
    print(itemse)
3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
result = 0
for x in my_dictionary:
      result += my_dictionary[x]
print(result)
3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
list = [1, 2, 3, 4, 5, 3, 2, 1]
print(set(list))
3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
     - найдите значения, которые встречаются в обоих множествах
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print(set1.intersection(set2))
     - найдите значения, которые не встречаются в обоих множествах
print(set1.symmetric_difference(set2))
     - проверьте являются ли эти множества подмножествами друг друга
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print(set2.issubset(set1))
print(set1.issubset(set2))