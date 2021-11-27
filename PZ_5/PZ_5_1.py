def Ramka(slovo):
    dlina = len(slovo)
    Ramka = ''
    for i in range(3):
        if i != 1:
            Ramka += '*' * (dlina + 2) + '\n'
        else:
            Ramka += "*" + slovo + "*" + '\n'
    return Ramka

res = Ramka(input("Введите слово: "))
print(res)