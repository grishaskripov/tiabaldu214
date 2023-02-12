# name_name = "Grisha"
# print("Hello", name_name)
# age = 32
# print(age)
# print(id(age))
# print(type(age))
# print(id(age))
# age = "hello"
# print(type(age))
#
# a = b = c = 1
# print(a, b, c)
# a, b, c = 5, "Hello", 9.2
# print(a, b, c)
# pi = 3.14
# print(pi)
# pi = 2
# print(pi)
#
# a = "5"
# b = 2
# print(int(a) + b)
#
# a = 1
# b = 2
# print("a =",a)
# print("b =",b)
# c = a
# a = b
# b = c
# a, b = b, a
import time

# print(6+2)
# print(6/2)
#
# number = 6+4*5**2+7
# print(number)
#
# number1 = 5+7+3
# print(number1)
# number2 = 5*7*3
# print(number2)
# number3 = (5*7*3)/3
# print(number3)

# num = 10
# num +=5 #num = num + 5
# print(num)
#
# num1 = 10
# num1 -=2
# print(num1)

# num = 4321
# a = num % 10
# print(a)
# num = num // 10
# print(num)
# b = num % 10
# print(b)
# num = num // 10
# print(num)
# c = num % 10
# print(c)
# num = num // 10
# print(num)
#
# print(a*1000+b*100+c*10+b)
#
# num = 4321
# res =  num % 10 * 1000
# num //= 10 #432
# res += num % 10 * 100
# num //=10 #43
# res += num % 10 * 10
# num //= 10 #4
# res += num % 10
# print(res)


# num1 = '2'
# num2 = 3
# res = int(num1) + num2
# print(res)

# name = input("Ваше имя: ")
# print(name)

# num = input("Число: ")
# st = input("Степень: ")
# num = int(num)
# st = int(st)
# res = num ** st
# print('Число', num, 'в степени', st, 'равно', res)

# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)


# age = int(input("Введите свой возраст: "))
# if age >= 18:
#    print("Доступ разрешен")
# else:
#    print("Доступ разрешен")
#
# a = 45
# b = 35
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a == b")

# a = int(input("Сторона первая: "))
# b = int(input("Сторона вторая: "))
# c = int(input("Сторона третяя: "))
# if a == b and b == c:
#     print("равносторонний")
# elif a == b or a == c or b == c:
#     print("равнобедренный")
# else:
#     print("разносторонний")


# day = int(input("День недели(цифрой): "))
# if 1<= day <= 5: #day >= 1 and day <=5:
#     print("Рабочий день", end="")
#     if day == 1:
#        print("Понедельник")
#     if day == 2:
#        print("Вторник")
#     if day == 3:
#        print("Среда")
#     if day == 4:
#        print("Четверг")
#     if day == 5:
#        print("Пятница")
# elif day == 6 or day == 7:
#     print("Выходной", end="")
#     if day == 6:
#        print("Суббота")
#     if day == 7:
#        print("Воскресенье")
# else:
#     print("noy")


# x = int(input('Делимое: '))
# y = int(input('Делитель: '))
# print(x / y if y != 0 else 'На ноль делить нельзя!')
#
# try:
#     x = input('Делимое: ')
#     y = input('Делитель: ')
#     print(int(x) + int(y))
# except(ValueError):
#     print(x + y)

# x = int(input('Делимое: '))
# y = int(input('Делитель: '))
# print(x / y if y != 0 else 'На ноль делить нельзя!')

# i = 2
# while i <= 20:
#     print(i, end="")
#     i += 2
#
#     i = 1
#     while i <= 10:
#         print(i * 2, end="")
#         i += 1
#
#         i = 1
#         while i <= 20:
#             if i % 2 == 0:
#             print(i, end="")
#             i += 1

# x, y = int(x), int(y)
# print(str(x) + str(y))

# i = 2
# while i <= 20:
#     print(i)
#     i += 2
#
#     m = 1
#     while True:
#         n = int(input('Число: '))
#         if n == 0:
#             break
#         m *= n
#     print('Произведение равно:', m)

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, '*', j, '=', i * j, '\t', end = '')
#         j += 1
#     print('')
#     i += 1

# for element in collection:
#     тело цикла
# for i in "Hello", "red", "blue", "yellow", 20, 0.3:
#     print(i)
# print(range(5))
# range(start, stop, step)
# for i in range(-16, -8, 1):
#     print(i, end=" ")
#
# print()
# i = 10
# while i > 0:
#     print(i, end=" ")
#     i -= 1
# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")
# num = input('Введите целое число: ')
# try:
#     num = int(num)
#     for i in range(1, num):
#         if i % 10 == i // 10:
#             print(i, end=' ')
# except ValueError:
#     print('Вас просили число!')
# for i in range(10, 100):  # 98  98 % 10 = 8  ==  98 // 10 = 9
#     if i % 10 == i // 10:
#         print(i, end=' ')
# for i in range(11, 101, 11):
#     print(i, end=" ")
# for i in range(3):
#     print(i, end=" ")
#     if i == 1:
#         break
# else:
#     print('\ndone')
# for i in range(3):
#     print("+++", i)
#     for j in range(2):
#         print("-----", j)
# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         print("*", end="")
#     print()
# w = int(input('W = '))
# h = int(input('H = '))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or j == 0 or i == h - 1 or j == w - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# a = [int(input('-> ')) for num in [0] * int(input('Count: '))]
#
# count = sum = 0
# for i in a:
#     if i != 0:
#         count += 1
#         sum += i
# print('Среднее: ', sum / count)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:  #
#         print(a[i], end=" ")

# Методы списков
# a = list(range(1, 8))
# print(a)
# a.append(99)  # добавляет элемент в конец списка
# print(a)
# a.extend([22, 11, 9])  # добавляет множество элементов в конец списка
# print(a)
# a.insert(0, 100)  # добавляет элемент в список. Первый параметр - индекс, второй - добавляемое значение
# print(a)
# a.extend('add')
# print(a)

# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("-> "))
#     s.append(x)
# print(s)

# s = []
# n = int(input('Введите количество элементов списка: '))
# for i in range(n):
#     x = int(input('Введите число кратное 3: '))
#     if x % 3 != 0:
#         print(x, 'не делится на 3 без остатка')
#     else:
#         s.append(x)
# print(s)
#
# s = []
# n = int(input('Количество элементов списка: '))
# for num in range(n):
#     x = int(input('Введите число кратное 3:  '))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, 'не делится на 3 без остатка')
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7, 2]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11, 12, 13, 2, 4]
# c = []

# if len(b) < len(a):
#     a, b = b, a
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])

# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)

# b = [11, 13, 12, 13, 2, 4, 13]
# b.remove(13)  # удаляет элемент из списка по значению, если элементов с заданным значением несколько, то удаляется
# # только первый
# print(b)
# a = 3
# if a in b:
#     b.remove(a)
# print(b)

# last = b.pop(1)  # c пустыми скобками - удаляет последний элемент из списка, с заданным индексом в скобках - удаление
# # по индексу
# print(b)
# print(last)
#
# b.clear()
# print(b)  # очищает список

# a = [int(input('-> ')) for num in ' ' * int(input('Count: '))]
# b = int(input('Index: '))
# a.pop(b)
# print(a)

# a = [9, 2, 7, 2, 4, 2, 3, 2]
# num = a.count(2)  # количество заданных значений в списке
# print(num)
# ind = a.index(2, 2, -1)  # возвращает первый индекс искомого значения. Также можно указать значения start и end
# print(ind)

# a = [9, 2, 7, 2, 4, 2, 3, 2]
# b = a.copy()
# print("a:", id(a))
# print("b:", id(b))
# a.append(20)
# b.remove(9)
# print("a:", a)
# print("b:", b)

# a = [9, 2, 7, 2, 4, 2, 3, 2]
# print(a)
# # a.reverse()  # перестраивает элементы списка в обратном порядке
# # print(a)
# a.sort()  # сортирует список, по умолчанию - по возрастанию, reverse=True - по убыванию
# print(a)
# #
# # b = ["Виталий", "Сергей", "Александр", "Анна"]
# # b.sort(key=len, reverse=True)
# # print(b)
#
# c = sorted(a)
# print(c)
# print(a)

# Генерация случайных данных

# import random
#
# print(random.random())
# print(random.randint(2, 9))  # от 2 по 9 (включительно)
# print(random.randrange(1, 9, 2))

# from random import randint, randrange
#
# print(randint(2, 9))
# print(randrange(1, 9, 2))

# from random import *
#
# print(randint(2, 9))
# print(randrange(1, 9, 2))


# import random as r
#
# print(r.randint(2, 9))
# print(r.randrange(1, 9, 2))
# print(r.uniform(10.5, 25.5))
# print(round(r.uniform(10.5, 25.5), 3))
#
# city = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# # city = [5, 3, 9, 7, 8, 6, 4, 2, 1]
# # print(r.choice(city))
# print(r.choices(city, k=2))
# r.shuffle(city)
# print(city)

# import random as r

# mas = [r.randint(-30, 30) for i in range(5)]
# print(mas)

# lst = ["5, 3, 2, 4, 1", "abc"]
# print(len(lst))
# print(max(lst))
# print(min(lst))
# print(sum(lst))

# from random import randint
#
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# c = a + b
# print("Третий список: ", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Элементы обоих списков без повторений", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Элементы общие для двух списков: ", c)
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)
#
# import random
# n = int(input("Размер списка: "))
# s = []
# while len(s) < n:
#     num = random.randrange(n)
#     if num not in s:
#         s.append(num)
# print(s)
#
# from random import randint
#
# w, h = 5, 3
# matrix = [[randint(10, 100) for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()
#
#
# w, h = 4, 3
# count = 0
# matrix = [[randint(-20, 10) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#         if x < 0:
#             count += 1
#     print()
# print('Количество отрицательных чисел:', count)

# import time
# import locale
# locale.setlocale(locale.LC_ALL, "en")
# seconds = time.time()
# print(seconds)
#
# local_time = time.ctime(seconds)
# print(local_time)
#
# res = time.localtime()
#

# pause = 5
# print("Program started...")
# time.sleep(pause)
# print(pause, "seconds")

# text = input("Название напоминания:")
# local_time = float(input("Через сколько секунд:"))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)

# start = time.monotonic()
# time.sleep(9)
# finish = time.monotonic()
# res = finish - start
# print(res, "sec.")

# a = 2
#
#
# def hello():
#     print("hello")
#
#
# hello()

def get_sum(a, b):
    x = 1
    print(x)
    print(a + b)

a = 2
b = 5
get_sum(a, b)


# Функции
# a = 2
#
#
# def hello(name, word):
#     print("Hello, ", name, ". Say ", word, sep="")
#
#
# hello("Irina", "hi")
# hello("Ivan", "hello")

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum("abc", "def")
# get_sum(2.5, 4.7)

# def symbol(count, a, b):
#     # print((a + b) * (count // 2) + a * (count % 2))
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#     # print("".join([a if i % 2 == 0 else b for i in range(count)]))
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")
#
#
# def get_sum(count, a, b):
#     print(''.join(a * (1 - i % 2) + b * (i % 2) for i in range(count)))
#
#
# get_sum(9, "+", "-")


# def get_sum(a, b):
#     return a + b
#
#
# x = 2
# y = 5
# w = get_sum(x, y)
# print(w * 2)

# Функции
# a = 2
#
#
# def hello(name, word):
#     print("Hello, ", name, ". Say ", word, sep="")
#
#
# hello("Irina", "hi")
# hello("Ivan", "hello")

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum("abc", "def")
# get_sum(2.5, 4.7)

# def symbol(count, a, b):
#     # print((a + b) * (count // 2) + a * (count % 2))
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#     # print("".join([a if i % 2 == 0 else b for i in range(count)]))
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")
#
#
# def get_sum(count, a, b):
#     print(''.join(a * (1 - i % 2) + b * (i % 2) for i in range(count)))
#
#
# get_sum(9, "+", "-")


# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")
#
# seconds = time.time()
# print(seconds)
#
# local_time = time.ctime(seconds)
# print(local_time)
#
# res = time.localtime()
# print(res)
# print(res.tm_year)
#
# print(time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime(4654414541)))
# print("Сегодня:", time.strftime("%B %d, %Y"))

# pause = 5
# print("Program started...")
# time.sleep(pause)
# print(pause, "seconds")

# text = input("Название напоминания: ")
# local_time = float(input("Через сколько минут: "))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res, "sec.")

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res, "sec.")

# def digits_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         if not even and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр: ")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print("Сумма нечетных цифр: ")
# print(digits_sum(9874023, even=False))
# print(digits_sum(38271, even=False))
# print(digits_sum(123456789, even=False))

# a = "Python"
# b = "Programming language"
# c = set(a) - set(b)
# for i in c:
#     print(i, end=" ")
#
# s1 = 'Python'
# s2 = 'Programing language'
# print(set(s1) - set(s2))

# list()
# tuple()
# set() - множество

# s = {'banana', 'apple', 'orange', 'apple', 'orange'}
# print(s)
# print(type(s))
# print(len(s))

# c = ['red', 'green', 'green', 'blue']
# a = set(c)
# print(type(a))
# print(a)

# numbers = [1, 2, 2, 3, 3, 4, 4, 5, 6]
# s = list({x for x in numbers if x % 2 == 0})
# print(s)


# def to_set(par):
#     st = set(par)
#     return st, len(st)
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))


# s = {'banana', 'apple', 'orange'}
# print('apple' in s)
# print('apple' not in s)
# print(s)
# for i in s:
#     print(i)

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {i for i in r if 'a' not in i}
# b = {"A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r}
# c = {"A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c'}
# print(a)
# print(b)
# print(c)
#
# for i in r:
#     if i[1] == 'c':
#         if i[0] == 'a':
#             print("A" + i[1:])
#         else:
#             print('B' + i[1:])
#
#
# for i in r:
#     if i[0] == 'a':
#         if i[1] == 'c':
#             print("A" + i[1:])
#     else:
#         if i[1] == 'c':
#             print('B' + i[1:])


# s = {'banana', 'apple', 'orange'}
# print(s)
# # s.add(4)  # добавляет элемент во множество
# # if 44 in s:
# #     s.remove(44)  # удаляет элемент по значению
# # s.discard(44)  # удаляет элемент по значению без генерации исключения
# a = s.pop()  # удаление первого элемента
# s.clear()  # полная очистка множества
# print(s)
# print(a)


# Операции над множествами
# a = {0, 1, 2, 3, 4}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b
# # c = a & b
# # a |= b
# # a &= b
# # c = b - a
# # a -= b
# # c = a ^ b
# # a ^= b
# c = a < b
# print(c)
# print(a)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))
# print(sum(s))

# s1 = 'Hello'
# s2 = "How are you"
# a = set(s1) & set(s2)
# for i in a:
#     print(i, end=" ")


# s1 = "Python"
# s2 = "Programming language"
# print(set(s1).difference(s2))
#
# s1 = 'Python'
# s2 = 'Programing language'
# print(set(s1) - set(s2))
#
# a = "Python"
# b = "Programming language"
# c = set(a) - set(b)
# for i in c:
#     print(i, end=" ")

# drawing = {'Марина', 'Женя', 'Света'}
# music = {'Костя', 'Женя', 'Илья'}
#
# one_hobby = drawing ^ music
# print(one_hobby)
# both_hobby = drawing & music
# print(both_hobby)
# drawing = drawing - both_hobby
# print(drawing)

# frozenset()

# s = frozenset([1, 2, 3, 4, 5])
# print(s)
#
# s1 = frozenset({"hello", "world"})
# print(s1)


# Словарь (dict)

# a = [1, 2, 3]
# d = {1: 'one', 'two': 2, 'three': 3, 'four': 3}
# print(a[0])
# print(d[1])

# d = {'one': 1, 'two': 2}
# d = dict(one=1, two=2)
# print(d)
# print(type(d))

# a = (
#     ('igor@gmail.com', 'Igor'),
#     ('irina@gmail.com', 'Irina'),
#     ('anna@gmail.com', 'Anna'),
# )
#
# b = dict(a)
# print(b)

# d = {i: 100 for i in range(2, 7)}
# print(d)
# print(d[3])
# d[3] = 15
# print(d)


# d = {0: 'text', 'one': 45, (1, 2.3): "Кортеж", 42: [2, 3, 6, 7], True: {1, 0}}
# print(d)
# print(d[42][1])
# print(d[(1, 2.3)])
# d[(1, 2.3)] = "Новое значение"
# print(d)
# print("one1" in d)
# key = 'one1'
# if key in d:
#     del d[key]
# print(d["one1"])
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом " + key + " нет в словаре")

# d = {0: 'text', 'one': 45, (1, 2.3): "Кортеж", 42: [2, 3, 6, 7], True: {1, 0}}
# print(d)
#
# for key in d:
#     print(key, "-> ", d[key])

# a = {"x1": 3, "x2": 7, "x3": 5, "x4": -1}
# s = 1
# for i in a:
#     s *= a[i]
# print(s)

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# d = {input("-> "): input("-> ") for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core i5-3450', 5, 6400],
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input('№: ')
#     if n != '0':
#         qty = int(input("Количество: "))
#         goods[n][1] = qty
#     else:
#         break
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб", sep="")
#
#
#
#     a = {"x1": 3, "x2": 7, "x3": 5, "x4": -1}
#     s = 1
#     for i in a:
#         s *= a[i]
#     print(s)
#
#     my_dict = {'one': 'first'}
#
#
#     def func(**data):
#         for key, value in data.items():
#             my_dict[key] = value
#         return my_dict
#
#
#     print(func(k1=22, k2=31, k3=11, k4=91))
#     print(func(name='Bob', age=31, weight=61, eyes_color='grey'))
#
#     res = []
#     for i in args:
#         res.append(int(reversed(str(num))))
#     return res
#
# def print_scores(student, *scores):
#     print("\nStudent Name:", student, end=", scores: ")
#     count = 0
#     for score in scores:
#         count += 1
#         if count!= len(scores):
#             print(score, end=", ")
#         else:
#             print(score)
#
#
#
# print_scores("Kate", 100, 95, 88, 92, 99)
# print_scores('Rick', 96, 20, 33, 56)
#
#
# my_dict = {'one': 'first'}
# def func(**data):
#     for key, value in data.items():
#         my_dict[key] = value
#     return my_dict
#
#
# print(func(k1=22, k2=31, k3=11, k4=91))
# print(func(name='Bob',age=31,weight=61,eyes_color='grey'))

# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#
#     s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(b, c))
#     return s
#
#
# print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(1, 6, 8))
# s = 0
#
#
# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#
#     global s
#     s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(b, c))
#
#
# rect_paral_square(2, 4, 6)
# print(s)
# rect_paral_square(5, 8, 2)
# print(s)
# rect_paral_square(1, 6, 8)
# print(s)


# def rect_paral_square(a, b, c):
#     s = 0
#
#     def rect_square(i, j):
#         nonlocal s
#         s += i * j
#
#     rect_square(a, b)
#     rect_square(a, c)
#     rect_square(b, c)
#     return 2 * s
#
#
# print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(1, 6, 8))

# def func(city):
#     s = 0  # 3  2
#
#     def wrap():
#         nonlocal s
#         s += 1
#         print(city, s)  # 3
#
#     return wrap
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res1()

# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def classifier(lower, upper):
#     def student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return student
#
#
# A = classifier(80, 100)
# B = classifier(70, 80)
# C = classifier(50, 70)
# D = classifier(0, 50)
# print("A =", A(students))
# print("B =", B(students))
# print("C =", C(students))
# print("D =", D(students))

# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         print("qqq")
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul())
# obj1()


# lambda (Анонимные функции)

# print((lambda x, y: x + y)(1, 2))
# c = (lambda x, y: x + y)('a', 'b')
# print(c)
# a = 5
# func = lambda x, y: x + y + a
# b = func(1, 2)
# print(b)
# # print(func('a', 'b'))
#
# (lambda: print("Hello"))()


# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# summ = lambda a=1, b=2, c=3: a + b + c
#
# print(summ(10, 20, 30))
# print(summ(10, 20))
# print(summ(10))
# print(summ())

# func = lambda *args: args
# #
# # print(func(1, 2, 3, 4, 5, 6, 7))
# # print(func())
#
#
# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#     print(t('abc_'))

def inc(n):
    return lambda x: n + x


f = inc(42)
print(f(3))

inc1 = (lambda n: lambda x: n + x)

f3 = inc1(42)
print(f3(3))
print("!!!", (lambda n: lambda x: n + x)(42)(3))


def inc2(n):
    def wrap(x):
        return n + x

    return wrap


f1 = inc2(42)
print(f1(3))


# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#
#     s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(b, c))
#     return s
#
#
# print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(1, 6, 8))
# s = 0
#
#
# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#
#     global s
#     s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(b, c))
#
#
# rect_paral_square(2, 4, 6)
# print(s)
# rect_paral_square(5, 8, 2)
# print(s)
# rect_paral_square(1, 6, 8)
# print(s)


# def rect_paral_square(a, b, c):
#     s = 0
#
#     def rect_square(i, j):
#         nonlocal s
#         s += i * j
#
#     rect_square(a, b)
#     rect_square(a, c)
#     rect_square(b, c)
#     return 2 * s
#
#
# print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(1, 6, 8))

# def func(city):
#     s = 0  # 3  2
#
#     def wrap():
#         nonlocal s
#         s += 1
#         print(city, s)  # 3
#
#     return wrap
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res1()

# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def classifier(lower, upper):
#     def student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return student
#
#
# A = classifier(80, 100)
# B = classifier(70, 80)
# C = classifier(50, 70)
# D = classifier(0, 50)
# print("A =", A(students))
# print("B =", B(students))
# print("C =", C(students))
# print("D =", D(students))

# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         print("qqq")
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul())
# obj1()


# lambda (Анонимные функции)

# print((lambda x, y: x + y)(1, 2))
# c = (lambda x, y: x + y)('a', 'b')
# print(c)
# a = 5
# func = lambda x, y: x + y + a
# b = func(1, 2)
# print(b)
# # print(func('a', 'b'))
#
# (lambda: print("Hello"))()


# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# summ = lambda a=1, b=2, c=3: a + b + c
#
# print(summ(10, 20, 30))
# print(summ(10, 20))
# print(summ(10))
# print(summ())

# func = lambda *args: args
# #
# # print(func(1, 2, 3, 4, 5, 6, 7))
# # print(func())
#
#
# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#     print(t('abc_'))

def inc(n):
    return lambda x: n + x


f = inc(42)
print(f(3))

inc1 = (lambda n: lambda x: n + x)

f3 = inc1(42)
print(f3(3))
print("!!!", (lambda n: lambda x: n + x)(42)(3))


def inc2(n):
    def wrap(x):
        return n + x

    return wrap


f1 = inc2(42)
print(f1(3))

# filter(func, iterable)

# t = ('abcd', 'abc', 'adefg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# z = [15, 37, 36, 26, 27, 35, 27, 20, 24, 3]
# res = list(filter(lambda a: 10 < a <= 20, z))
# print(res)


# from random import randint
#
# lst = [randint(1, 40) for i in range(10)]
# print(lst)
# lst2 = list(filter(lambda s: 10 <= s <= 20, lst))
# print(lst2)

# nums = [45, 55, 60, 37, 100, 105, 220]
# res = list(filter(lambda x: x % 15 == 0, nums))
# print(res)

# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))  # (1, 3, 5, 7, 9)
# print(m)
#
# m1 = [x ** 2 for x in range(10) if x % 2]
# print(m1)


# Декораторы


# def hello():
#     return 'Hello, I am func "hello"'
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# test = hello
# print(test())


# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#     return func_wrapper
#
#
# def func_test():
#     print('Hello, I am func "func_test"')
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):  # декорирующая функция
#     def func_wrapper():
#         print('*' * 40)
#         func()
#         print('*' * 40)
#     return func_wrapper
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print('Hello, I am func "func_test"')
#
#
# func_test()
# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()
# hello()
# hello()


# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Данные:", arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Назарова")

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print(*args)
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# @args_decorator
# def print_full_name_1(first, second, last):
#     print("Меня зовут", first, second, last)
#
#
# print_full_name("Ирина", "Назарова")
# print()
# print_full_name_1("Виктор", last="Назаров", second="Федорович")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)
#
# def decor(*args):
#     def args_dec(fn):
#         def wrap(x, y):
#             # print(args[0], x, args[1], y, "=", end=" ")
#             print(*args, end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)


# def multiply(num):
#     def decor(fn):
#         def wrap(mult):
#             return num * fn(mult)
#
#         return wrap
#
#     return decor
#
#
# @multiply(3)
# def return_num(ch):
#     return ch
#
#
# print(return_num(5))

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Некорректный тип данных", f_args[i])  # print("Некорректный тип данных!")
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Некорректный тип данных", f_kwargs[k])
#
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello"):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Doge"))
# print(typed_fn2("Hello", "World", "!"))
# print(typed_fn3("Hello", "World", z=5))


# def args_decorator(tx=None, decorator_text=""):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end="")
#             func(*args)
#
#         return wrap
#
#     if tx is None:
#         return my_decorator
#     else:
#         return my_decorator(tx)
#
#
# @args_decorator(decorator_text="Hello, ")
# def hello_world(text):
#     print(text)
#
#
# @args_decorator
# def hello_world2(text):
#     print(text)
#
#
# hello_world("world!")
# hello_world2("Hi!")
#
# str1 = "Я изучая Nython. Мне нравится Nython. Nython очень интересный язык программирования."

# s1 = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:58. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."# rg = r'[0-2][0-9]:[0-5][0-9]'# print(re.findall(rg, s1)) 

# st = r"Замените в этой стрОке все пОявления буквы ""О"", крОме первОгО и пОследнегО вхождения."print(st.replace("О", "о"))
#
#
# print(re.findall('[+]?7\d{9}', s))

# s = input('Введите дату в формате dd-mm-YYYY:')print(s)reg = r'([1-3]\w)-([0-1]\w)-([1-2]\w{3})'print(re.findall(reg, s))
#
# s = "<p>Изображение <img alt='картинка' src ='bg.jpg'> - фон страницы</p>"reg = r'<img\s+[^>]*src\s*=>'print(re.findall(reg, s))