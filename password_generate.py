from random import *
print("""Добро пожаловать в Генератор сложный паролей!
Программа "Генератор сложных паролей" разработана для создания надежных и безопасных паролей как автоматически, так и по требованиям, указанным пользователем. 
Это инструмент, который поможет пользователям генерировать уникальные пароли для обеспечения безопасности и конфиденциальности их данных.""")
def variants():
    print("1. Создать пароль автоматически")
    print("2. Создать пароль по требованиям")
    print("0. Выход")
    print("Введите ваше число:")
variants()
big_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_letter = "abcdefghijklmnopqrstuvwxyz"
numbers = randint(0 , 10)
symbols = "!@#$~%^&*_?><"
all_b = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$~%^&*_?><"
def automatic_password(len_pass):
    b = ""
    while len(b) != len_pass:
        c = choice(all_b)
        if c not in b:
            b += c
    print(b)
s = input()
while s != "0":
    if s == "1":
        print("Введите длину вашего пароля:")
        n = int(input())
        automatic_password(n)
        variants()
        s = input()
    if s == "0":
        print("Спасибо за использование!")
        
