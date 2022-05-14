# В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в
# 2 раза.

import random


m = int(input('m = '))  # задаём размеры матрицы
n = int(input('n = '))

while True: # создаём матрицу, выводим матрицу и проверяем что она квадратная
    if m == n:
        Matrix = [[random.randint(-11, 11) for j in range(n)] for i in range(m)]
        print('Матрица:')

        for i in range(m):
            print(Matrix[i])
        break
    else:
        m = int(input('Ошибка! Напиши заново! m = '))
        n = int(input('n = '))

count = [Matrix[i][i] for i in range(m) for j in range(1)] # находим главную диагональ

for i in range(m):
    for j in range(n):
        if i != j:
            Matrix[i][j] *= 2 # умножаем все на 2, кроме главной диагонали

print("Новая матрица:")
for i in range(m):  # выводим
    print(Matrix[i])