# Дано целое число, большее 999. Используя одну операцию деления нацело и
# одну операцию взятия остатка от деления, найти цифру, соответствующую разряду тысяч в записи
# этого числа.


ches = (input("Введите число больше  999: "))

#Проверяем целое число или нет
while True:
    try:
        ches = int(ches)
        break
    except ValueError:
        print("Неправильно ввели!")
        ches = (input("Введите число больше  999: "))

#Проверяем условия и выполняем действия
while True:
    if ches > 999:
        ches = ches // 1000
        ches = ches % 10
        break
    else:
        print("Ошибка")
        ches = (input("Введите число больше  999: "))
print(ches)