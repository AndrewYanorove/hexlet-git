import secrets
from colorama import Fore, Style
from random import *
class PasswordGenerator:
    def __init__(self):
        self.big_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.small_letter = "abcdefghijklmnopqrstuvwxyz"
        self.numbers = "0123456789"
        self.symbols = "!@#$~%^&*_?"
        self.all_b = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$~%^&*_?"
    
    def auto_generate_password(self, length):
        password = ''.join(secrets.choice(self.all_b) for _ in range(length))
        return password
    
    def manual_generate_password(self, length, use_uppercase, use_lowercase, use_numbers, use_symbols):
        all_symbols = ""
        password = ""
        
        if use_uppercase:
            all_symbols += self.big_letters
            
        if use_lowercase:
            all_symbols += self.small_letter
            
        if use_numbers:
            all_symbols += self.numbers
            
        if use_symbols:
            all_symbols += self.symbols
            
        if all_symbols != "":
            for _ in range(length):
                password += secrets.choice(all_symbols)
            return password
        else:
            return "Вы должны выбрать хотя бы 1 условие!"
    def save_to_file(self, password, filename="password.txt"):
        try:
            with open(filename, "a") as file:
                file.write(password + "\n")
        except FileNotFoundError:
            with open(filename, "w") as file:
                file.write(password + "\n")
    def show_menu(self):
        print(f"{Fore.CYAN}1. Создать пароль автоматически")
        print(f"2. Создать пароль по требованиям")
        print("0. Выход")
        return input(f"{Fore.YELLOW}Введите ваш выбор: ")

    def main(self):
        choice = self.show_menu()
        while choice != "0":
            if choice == "1":
                length = int(input("Введите длину пароля: "))
                print(f"{Fore.GREEN}Сгенерированный пароль:")
                generated_password = self.auto_generate_password(length)
                print("")
                print(generated_password)
                self.save_to_file(generated_password)
            elif choice == "2":
                length = int(input("Введите длину пароля: "))
                use_upper = input("Использовать прописные буквы? (1. да | 2. нет): ").lower() == "1"
                use_lower = input("Использовать строчные буквы? (1. да | 2. нет): ").lower() == "1"
                use_nums = input("Использовать цифры? (1. да | 2. нет): ").lower() == "1"
                use_syms = input("Использовать символы? (1. да | 2. нет): ").lower() == "1"
                print(f"{Fore.GREEN}Сгенерированный пароль:")
                generated_password = self.manual_generate_password(length, use_upper, use_lower, use_nums, use_syms)
                print("")
                print(generated_password)
                self.save_to_file(generated_password)
            
            print("")
            print(f"{Fore.MAGENTA}Операция завершена.")
            choice = self.show_menu()

        print(f"{Fore.YELLOW}Спасибо за использование!")

generator = PasswordGenerator()
generator.main()
        
