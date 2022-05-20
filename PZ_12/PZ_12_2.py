# Дано целое число. Если оно является положительным, то прибавить к нему 1; в противном
# случае вычесть из него 2. Вывести полученное число.

from tkinter import *


def proverka(): # Проверка
    ches = cheslo.get()
    try:
        ches = int(ches)
        veches()
    except ValueError:
        iotg['text'] = 'Неверные еденицы данных'
        cheslo.delete(0, END)


def veches(): # условие задачи
    ches = cheslo.get()
    ches = int(ches)
    if ches > 0:
        iotg['text'] = ches + 1
        cheslo.delete(0, END)
    elif ches < 0:
        iotg['text'] = ches - 2
        cheslo.delete(0, END)
    else:
        iotg['text'] = 'Ошибка'
        cheslo.delete(0, END)


root = Tk() # Окно программы, кнопки и т.д
root.geometry('300x200')
root.config(bg='gray')
root.resizable(height=False, width=False)
root.title('Практическая работа 12 №2')

zadacha = Label(text='Дано целое число. Если оно является \n положительным, то прибавить к нему 1; \n \
 в противном случае вычесть из него 2. \n Вывести полученное число.')
zadacha.grid(row=0, columnspan=2, stick='wens')

cheslo1_text = Label(root, text='Введите целое число: ')
cheslo1_text.grid(row=1, column=0, pady=5, stick='wens')

cheslo = Entry(root)
cheslo.grid(row=1, column=1, stick='wens', pady=5)

iotg = Button(text='Нажмите чтобы узнать итоговое \n число.', bd=5, font=('Arial', 12), fg='red',
              command=lambda: proverka())
iotg.grid(row=2, columnspan=2, stick='wens', padx=5, pady=5)

root.grid_rowconfigure(0, minsize=60)
root.grid_rowconfigure(1, minsize=20)
root.grid_rowconfigure(2, minsize=100)

root.grid_columnconfigure(0, minsize=150)
root.grid_columnconfigure(1, minsize=150)

root.mainloop()
