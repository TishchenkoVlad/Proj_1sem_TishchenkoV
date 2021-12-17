# Дан список игрушек. Некоторые игрушки из этого списка имеются в N детских садах.
# Определить, каких игрушек их этого списка нет ни в одном из детских садов и какие есть в
# каждом из них.

spisok_igr = {"кубик", "мяч", "машинка", "кукла"} # Создаём множество
N = int(input("Введите количество детских садов: "))
slov = {}
for i in range(N):         # Добавляем ключи и элементы в словарь
    key = input("Детский сад: ")
    L = int(input("Введите количество игрушек в детском саду '" + key + "': "))
    val = []
    for j in range(L):
        val.append(input("Введите наименование игрушки: "))
    slov[key] = val

ds_toys = set()      # Создаём пустое множество
for key in slov:          # Находим каких игрушек нет в детских садиках
    for t in range(len(slov.get(key))):
        ds_toys.add(slov.get(key)[t])
if len(spisok_igr - ds_toys) > 0:
    print("Нет ни в одном из детских садов: ", spisok_igr - ds_toys)

ds_toys = set()
for key in spisok_igr:      # Находим игрушки, которые находятся в каждом детском садике
    cnt = 0  # Счётчик
    for j in slov:
        if key in slov.get(j):
            cnt += 1
    if cnt == N:
        ds_toys.add(key)

if len(ds_toys) > 0:
    print("Есть в каждом из детских садов: ", ds_toys)