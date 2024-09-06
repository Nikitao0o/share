

#Задание 1
def greet(name):
    """Выводит приветственное сообщение для переданного имени"""
    print("Hello, ", name, "!", sep="")
#greet(input())
def square(number):
    """Возвращает квадрат от переданного числа"""
    return number*number
#print(square(int(input())))
def max_of_two(x ,y):
    """ Возвращает большее из переданных чисел"""
    return max(x,y)
#print(max_of_two(int(input(), int(input()))))

#Задание 2

def describe_person(name, age=30):
    """принимает имя и возраст человека, и печатает эту информацию в читаемом виде"""
    print("Ваше имя:", name)
    if age%10 in [1,2,3,4]:
        gl = "года"
    else:
        gl = "лет"
    print("Ваш возраст:", age, gl)

#describe_person(input(), int(input()))

import math
def is_prime(number):
    """Возвращает True, если число простое и False в обратном случае"""
    if number%2 == 0:
        return False
    for i in range(3, math.ceil(math.sqrt(number))+1, 2):
        if number%i == 0:
            return False
    return True
#print(is_prime(int(input())))
