# Дан список A размера N. Сформировать новый список B того же размера, элементы
# которого определяются следующим образом:
# BK = 2*AK, если AK < 5,
# AK/2 в противном случае.

N = int(input("N: "))  # Вводим элементы массива
A = []
for i in range(N):     # Добавляем в массив
    A.append(int(input()))
B = []

for i in range(len(A)):  # Выполняем условие задачи
    if A[i] < 5:
        C = 2 * A[i]
        B.append(int(C))
    else:
        C = A[i] / 2
        B.append(round(float(C), 1))

print(B)