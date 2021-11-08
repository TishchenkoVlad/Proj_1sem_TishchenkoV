#Дано целое число. Если оно является положительным, то прибавить к нему 1; в противном
#случае вычесть из него 2. Вывести полученное число.

ches = input("Введите целое число: ") #Вводим целое число

# Проверка
while True:
    try:
        ches = int(ches)
        break
    except ValueError:
        print("Ошибка!")
        ches = input("Введите целое число ")

# Проверяем условия
if ches > 0:
    ches = ches + 1
elif ches < 0:
    ches = ches - 2
else:
    pass

# Выводим ответ
print(ches)