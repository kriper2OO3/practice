def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

user_input = input("Введите строку: ")

if is_palindrome(user_input):
    print("Да, это палиндром.")
else:
    print("Нет, это не палиндром.")
    
# добавлена проверка на число
number_input = input("Введите строку для проверки, является ли она числом: ")
if number_input.isdigit():
    print(f"{number_input} - это число.")
else:
    print(f"{number_input} - это не число.")
