# В матрице найти максимальный положительный элемент, кратный 4

import random


m = int(input('m = ')) # задаём размеры матрицы
n = int(input('n = '))


Matrix = [[random.randint(-11, 11) for j in range(n)] for i in range(m)] # создаём матрицу
print('Матрица:')

for i in range(m): # выводим матрицу
    print(Matrix[i])


count = [Matrix[i][j] for i in range(m) for j in range(n) if Matrix[i][j] > 0]
print("Положительные значения:", count) # находим положительные значения

if len(count) != 0:
    countmax = max(count)

    while True:      # находим кратное 4
        if countmax % 4 == 0:
            print(countmax)
            break
        elif countmax % 4 != 0:
            if len(count) != 0:
                countmax = max(count)
                count_new = count.pop(count.index(max(count)))
            else:
                print("Нет элемента")
                break
        else:
            print("Нет элемента")
            break
else:
    print("Нет положительных элементов")