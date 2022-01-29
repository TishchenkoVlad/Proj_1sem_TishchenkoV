# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Содержимое первого файла:
# Четные элементы:
# Произведение четных элементов:
# Минимальный элемент:
# Содержимое второго файла:
# Нечетные элементы:
# Количество нечетных элементов:
# Сумма нечетных элементов:





strok1 = str("1, 4, -10, 7, -2") # Задаём строчки
strok2 = str("3, -6, 9, 4, -30")

strokl1 = strok1.split(', ') # Превращаем строку в список
strokl2 = strok2.split(', ')

sym = 0 # Задаём счётчики
proiz = 1
chet = 0


my_file = open("File1.txt", "w+") # Создаём файлы
my_file.write(strok1)
my_file.close()


my_file = open("File2.txt", "w+")
my_file.write(strok2)
my_file.close()

cet = [] # Создаём дополнительные списки
nocet = []
for i in range(len(strokl1)): # Выполняем условие задачи
    if int(strokl1[i]) % 2 == 0:
        res1 = strokl1[i]
        cet.append(res1)
        proiz *= int(strokl1[i])
        #print(res1)

#print(", ".join(cet))

res2 = min(strokl1)
#print(res2)
#print(proiz)

for i in range(len(strokl2)):
    if int(strokl2[i]) % 2 != 0:
        res12 = strokl2[i]
        nocet.append(res12)
        chet += 1
        #print(res12)
        sym += int(res12)
#print(sym)
#print(chet)


my_file = open("newfile.txt", "w+") # Записываем результат в 3 файл
#my_file.write("Содержимое первого файла:")
print("Содержимое первого файла:", open("File1.txt").read(), file=my_file)
print("Четные элементы:", ", ".join(cet), file=my_file)
print("Произведение четных элементов:", str(proiz), file=my_file)
print("Минимальный элемент:", str(res2), '\n', file=my_file)
print("Содержимое второго файла:", open("File2.txt").read(), file=my_file)
print("Нечетные элементы:", ", ".join(nocet), file=my_file)
print("Количество нечетных элементов:", str(chet), file=my_file)
print("Сумма нечетных элементов:", str(sym), file=my_file)
my_file.close()




#print(a1)
#print(strokl2)