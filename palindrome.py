def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

user_input = input("Введите строку: ")

if is_palindrome(user_input):
    print("Да, это палиндром.")
else:
    print("Нет, это не палиндром.")
