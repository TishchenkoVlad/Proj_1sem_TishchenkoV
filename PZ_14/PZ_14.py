# Из исходного текстового файла (ip_address.txt) из раздела «Зарезервированные
# адреса» перенести в первый файл строки с ненулевыми первым и вторым октетами,
# а во второй – все остальные. Посчитать количество полученных строк в каждом
# файле

import re

chet1 = 0
chet2 = 0

check = False # Задаём флаг

f = open('ip_address.txt', 'r') # Открываем файл и создаём два других
res1 = open('result1.txt', 'w')
res2 = open('result2.txt', 'w')

for str in open('ip_address.txt', encoding='UTF-8'): # Пробегаемся по файлу
    #print(str)
    flag = str.find('Зарезервированные адреса') # Находим строку
    if flag != -1:
        check = True
    if check:
        point = str.find('.')  # Находим точку
        if point < 4 and point > 0:  # Находим позицию точки
            #print(str)
            #print(str[:point])
            match = re.match(r'[0][.][0][.]', str) # Проверка октетов
            if match:
                chet1 += 1
                res1.write(str)
            else:
                chet2 += 1
                res2.write(str)

print("В первом файле:", chet1, "строка")
print("Во втором файле:", chet2, "строк")




f.close()
res1.close()
res2.close()
