# Дан список игрушек. Некоторые игрушки из этого списка имеются в N детских садах.
# Определить, каких игрушек их этого списка нет ни в одном из детских садов и какие есть в
# каждом из них.

spisok_igr = {"кубик", "мяч", "машинка", "кукла"} # Создаём множество
slov = {"Детский сад 1": "кубик", "Детский сад 2": ["кубик", "машинка", "мишка"]}
print(slov)


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
    if cnt == 2:
        ds_toys.add(key)

if len(ds_toys) > 0:
    print("Есть в каждом из детских садов: ", ds_toys)