# Из списка: ['Валентин', 'Петр', 'Анна', 'Евгений', 'Константин', 'Валерия', 'Юлия']
# получить новый список, в котором длина слов не превышает 5 символов.


n = ['Валентин', 'Петр', 'Анна', 'Евгений', 'Константин', 'Валерия', 'Юлия']
new_n = [i for i in n if len(i) <= 5] # Проверяем длинну имён
print(new_n)