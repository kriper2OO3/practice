def calc():
    op = input("Выберите операцию (+, -, *, /): ")
    a, b = float(input("Первое число: ")), float(input("Второе число: "))

    if (op == '+'): res = a + b
    elif (op == '-'): res = a - b
    elif (op == '*'): res = a * b
    elif (op == '/'): 
        if b == 0: res = "Ошибка: деление на ноль"
        else: res = a / b
    else: res = "Некорректная операция"
    
    return res

result = calc()
print(f"Результат операции: {result}")
