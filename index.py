# 1
# a = int(input("Введите число:"))
# if a / 2 == 0:
#     print("Число четное")
# else:
#     print("Число нечетное")
# 2
# A = []  
# min_ = float('inf')                         
# a = int(input('Введите целое число...'))   
# c = int(input('Введите целое число...'))
# d = int(input('Введите целое число...'))
# e = int(input('Введите целое число...'))
# f = int(input('Введите целое число...'))
# A += a, c, d, e, f
# for i in A:
#     if i < min_:                            
#         min_ = i                            
# print(f'Минимальное: {min_}' )
# 3
# slovo = str(input("What is your word: "))
# a = slovo[::-1]
# if slovo == a:
#   print("yes it is palindrom")
# else:
#   print("no  it is not palindrom")
# 4 
# n = int(input("Введите число n: "))
# summa = 0
# for i in range(1, n + 1):
#     summa += i  
# print("Сумма всех чисел от 1 до", n, "равна", summa)

# 5
# n = int(input("Введите число n: "))
# for i in range(1, n):
#     for j in range(1, n):
#         print("%4d" % (i * j), end='')
#         print()
# 6
# A = []
# i = int(input("Введите число: "))
# b = int(input("Введите число: "))
# c = int(input("Введите число: "))
# d = int(input("Введите число: "))
# e = int(input("Введите число: "))
# A += i, b, c, d, e
# print(sorted(A))
# 7
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# def prime_numbers(n):
#     primes = []
#     for i in range(2, n + 1):
#         if is_prime(i):
#             primes.append(i)
#     return primes
# n = int(input("Введите число n: "))
# primes = prime_numbers(n)
# print("Простые числа до", n, ":", primes)
# 8
# s = input("n = ")
# words = s.split(" ")
# num_words = len(words)
# print(num_words)
#9
# numbers = input("Введите числа через пробел: ")
# numbers_list = list(map(int, numbers.split()))
# reversed_numbers = numbers_list[::-1]
# print("Перевёрнутый список:", reversed_numbers)
# 10
# list_num = input("Введите числа через пробел:  ")
# b = list(map(int, list_num.split()))
# a = list(dict.fromkeys(b))
# print(a)
# 11
# first = [12, 'ee', 4, 76, 'bb']
# sec = [23, 'ee', 41, 12, 'bs']
# c = []
# for i in first:
#     if i in sec:
#         c.append(i)
# print(c)
# 12
# first = list(map(int, input("Введите первое слово: ").split()))
# second = list(map(int, input("Введите второе слово: ").split()))
# common_elements = list(set(first) & set(second))
# print(common_elements)
# 13
# n = int(input("Введите число n: "))
# i = 1  
# while i <= n:  
#     print(i)
#     i += 1  
# 14 
# n = int(input("Введите число n: "))
# sum = 0  
# i = 1  
# while i <= n:  
#     sum += i  
#     i += 1  
# print("Сумма всех чисел от 1 до", n, "равна", sum)
# 15
# n = int(input("Введите пароль: "))
# while n != 123:
#     print("Пароль не верен попробуйте еще раз")
#     n = int(input("Введите пароль: "))    
# if n == 123:
#     print("пароль верный")   
# 16 

# first = list(map(int, input("Введите числа (завершите ввод 0): ").split()))

# while True:
#     if 0 in first:
#         first.remove(0)
#         print("Наибольшее число:", max(first) if first else "Нет введенных чисел")
#         break
# 17
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def introduce(self):
#         a = input("Введите имя человека ")    
#         b = int(input("Введите возраст человека "))
#         return f"Имя пользователя {a}, возраст {b}"
    
# p = Person("", int())
# print(p.introduce())
# 18 
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#             return self.width * self.height  
#     def perimetr(self): 
#             return (self.width * self.height) * 2   
        

# r = Rectangle(5, 10)
# print("Площадь равна:", r.area(), "Периметр равен ", r.perimetr())  
# 19
# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
# class GraduateStudent(Student):
#     def __init__(self, name, grades, speciality):
#         super().__init__(name, grades)
#         self.speciality = speciality
#     def job(self):    
#         return f"Your name is {self.name}, Gardes are {self.grades}, Your thesis {self.speciality}"

# graduate = GraduateStudent("Alex", 12, "good")
# print(graduate.job())
# 20
# a = [1, 1, 2, 3, 5, 8, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i < 5:
#         print(i)
# 21
# a = [1, 1, 2, 3, 5, 8, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 13, 20, 32, 55, 90]
# for i in a:
#     if i in b:
#         print(i)
# 22
# people = { "Выся": 25, "Beka": 12, "alex": 1, "anna": 21,}
# sorted_people = sorted(people.items(), key=lambda item: item[1])
# sorted_people_2 = sorted(people.items(), key=lambda item: item[1], reverse=True)
# print(sorted_people)
# print(sorted_people_2)
# 23
# di = {'a': 500, 'b': 5874,  'c': 560,  'd': 400,  'e': 5874,  'f': 20}
# print(sorted(di, key=di.get)[-3:])
# 24 
# a = " a1_ dudhush_ahyh, whshbd_jsjj"
# print(a.count("_"))
# 25
# a = input("введите оператичексое выражение + - * / ")
# b = int(input("введите первое число "))
# с = int(input("введите второе число "))
# if a == "+":
#     print("your answer", b + с)
# elif a == "-":
#     print("your answer", b - с)
# elif a == "*":
#     print("your answer", b * с)
# elif a == "/":
#     print("your answer", b / с)
# d = input("хотите добавить еще что-то?  yes/no")
# if d == "yes":
#     r = int(input("введите   первое число "))
#     k = int(input("введите  второе число "))
#     m = input("Доступные операции (**) ")
    
#     print("answer:", r ** k )
# elif d == "no":
#     print("Операция закончена")    
# 26
# def check_even_odd():
#     num = int(input("Enter a number: "))
#     if num % 2 == 0:
#         print("odd number")
#     else:
#         print("even number")
# import random

# def guess_number():
#     number = random.randint(1, 100)
#     tries = 0

#     print("Я загадал число от 1 до 100. Попробуй угадать его.")

#     while True:
#         guess = int(input("Твоя догадка: "))
#         tries += 1

#         if guess < number:
#             print("Мало.")
#         elif guess > number:
#             print("Много.")
#         else:
#             print(f"Ты угадал число {number} за {tries} попыток!")
#             break

# if __name__ == "__main__":
#     guess_number()
# 27

# def sum_of_list(numbers):
#     return sum(numbers)
# my_list = [1, 2, 3, 4, 5]
# print(f"Сумма списка {my_list} = {sum_of_list(my_list)}")
# another_list = [10, 20, 30, 40, 50]
# print(f"Сумма списка {another_list} = {sum_of_list(another_list)}")


# file1 = "result.txt"

# class Calculator:
#     def __init__(self, a, b, operation):
#         self.a = a
#         self.b = b
#         self.operation = operation
#         self.result = 0
    
#     def calculate(self):
#         if self.operation == "*":
#             self.result = self.a * self.b
#         elif self.operation == "+":
#             self.result = self.a + self.b
#         elif self.operation == "-":
#             self.result = self.a - self.b
#         elif self.operation == "/":
#             self.result = self.a / self.b
#         elif self.operation == "**":
#             self.result = self.a ** self.b
#         else:
#             print("Ввели не математическую операцию")
#             return

#         self.save_result()

#     def save_result(self):
#         with open(file1, "w") as file:
#             file.write(f"first: {self.a} \nsecond: {self.b} \noperation: {self.operation} \nresult: {self.result} \n")

# try:
#     a = float(input("Введите число:  "))
#     b = float(input("Введите второе число: "))
    
#     # Convert to int if the number is a whole number
#     a = int(a) if a.is_integer() else a
#     b = int(b) if b.is_integer() else b
    
#     operation = input("Что хочешь сделать?:  ")
    
#     calc = Calculator(a, b, operation)
#     calc.calculate()

# except ValueError:
#     print("Вы сделали неправильно")

# file1 = "result.txt"
# try:
    

#     a = float(input("Введите число:  "))
#     b = float(input("Введите второе число: "))
#     c = input("operation? ")


#     a = int(a) if a.is_integer() else a
#     b = int(b) if b.is_integer() else b


#     if c == "+":
#         d = a + b
#     elif c == "-":
#         d = a - b
#     elif c == "*":
#         d = a * b
#     elif c == "/":
#         d = a / b if b != 0 else "Error: Division by zero"
#     elif c == "**":
#         d = a ** b
#     else:
#         print("Ввели не математическую операцию")
#         exit()
#     def save_result(a, b, c, d):
#         if isinstance(d, (int, float)):  
#             with open(file1, "a") as file:
#                 file.write(f"first: {a} \nsecond: {b} \noperation: {c} \nresult: {d} \n")
#         else:
#             print(d)
# except ValueError:
#     print("Вы сделали неправильно или указали буквы")
# save_result(a, b, c, d)            
            
# class Nikola:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def description(self):
#         name = input("What is your name: ")
#         if name == "Николай":
#             print(f"Я {self.name}, Мне {self.age}")
#         elif name  != "Николай":
#             print(f"Я не {name}, а 'Nikolay'")
# nikola =  Nikola("Николай", 25)
# nikola.description()

class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self, a, b, c):
        if a > 0 and b > 0 and c > 0:
            if a + b > c and a + c > b and b + c > a:
                print("Ура, можно построить треугольник")
            else:
                print("Из этих отрезков нельзя построить треугольник")
        else:
            print("C отрицательными числами ничего не выйдет")

try:
    triangle = TriangleChecker(1, 2, 3)
    triangle.is_triangle(2, 2, 2)
except TypeError:
    print("Вы ввели не числа")

        





    
   
   




    
    