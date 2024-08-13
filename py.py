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
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
class GraduateStudent(Student):
    def __init__(self, name, grades, speciality):
        super().__init__(name, grades)
        self.speciality = speciality
    def job(self):    
        return f"Your name is {self.name}, Gardes are {self.grades}, Your thesis {self.speciality}"

graduate = GraduateStudent("Alex", 12, "good")
print(graduate.job())



    
   
   




    
    

