# Дан целочисленный список размера N, не содержащий одинаковых чисел. Проверить,
# образуют ли его элементы арифметическую прогрессию. Если образуют, то вывести
# разность прогрессии, если нет — вывести 0.




import sys

N = int(input("Введите размер массива: "))
spisok = []
for i in range(N):    # Ввод вручную элементов массива
    spisok.append(int(input()))
print(spisok)
for i in range(len(spisok)):     # Проверка повторяющихся чисел
    for j in range(len(spisok) - 1):
        if spisok[0] != spisok[j + 1]:
            continue
        else:
            print("Ошибка")
            sys.exit()
    spisok.append(spisok[0])
    spisok = spisok[1:]

d = spisok[1] - spisok[0]    # Вводим формулу разности арифмитической прогрессии
i = 1
flag = True
while flag and (i < N):      # Цикл с условием на арифмитическую прогрессию
    if spisok[i] - spisok[i - 1] != d:
        flag = False
        break
    i += 1
if flag:
    print(d)
else:
    print(0)
