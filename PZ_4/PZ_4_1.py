# Даны целые положительные числа N и K. Найти сумму 1 K + 2 К + ... + N K .

n = input("Введите целое число: ") # Вводим переменные и  счётчики
k = input("Введите целое число: ")
g = 0
ches = 1

while True: # Проверка на ошибки
    try:
        n = int(n)
        k = int(k)
        break
    except ValueError:
        print("Ошибка")
        n = input("Введите целое число: ")
        k = input("Введите целое число: ")

while ches != n + 1: # Условие
    s = ches ** k
    ches += 1
    g += s

print(g)