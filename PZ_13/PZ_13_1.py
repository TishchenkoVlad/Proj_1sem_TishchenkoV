# .В последовательности на n целых элементов в последней ее половине найти
# сумму элементов.

from random import * # Импортируем библиотеку

a = int(input("Введите число элементов: "))
numbers = [randrange(-10, 10) for i in range(a)] # Все элементы добавляем в список
print(numbers)

numbers = [i for i in numbers[a//2:]]  # Выполняем действия
print(sum(numbers))