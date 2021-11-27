# Дано трехзначное число. Проверить истинность высказывания: «Цифры данного числа
# образуют возрастающую или убывающую последовательность».

import sys

ches1 = input("Введите первую цифру: ")  # Вводим цифры
ches2 = input("Введите вторую цифру: ")
ches3 = input("Введите третью цифру: ")

# Проверка
while True:
    try:
        ches1 = int(ches1)
        ches2 = int(ches2)
        ches3 = int(ches3)
        break
    except ValueError:
        print("Ошибка")
        ches1 = input("Введите первую цифру: ")
        ches2 = input("Введите вторую цифру: ")
        ches3 = input("Введите третью цифру: ")

# Проверяем условия и выводим ответ
while True:
    if 0 < ches1 < 10:
        pass
    elif 0 < ches2 < 10:
        pass
    elif 0 < ches3 < 10:
        pass
    else:
        print("Ошибка")
        sys.exit()
    break

print((ches1 > ches2 > ches3) or (ches1 < ches2 < ches3))

# if ches1 > ches2 > ches3:
#     print(True)
# elif ches1 < ches2 < ches3:
#     print(True)
# else:
#     print(False)
