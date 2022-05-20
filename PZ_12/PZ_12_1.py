#В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
#его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
#приближенный к оригиналу (см. таблицу 1).


from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def button_clicked():
    print("Форма заполнена") # сообщение при заполнение данных

def close():
    root.destroy() # закрытие
    root.quit()

root=Tk() # создание окна
root.title("Онлайн заказ")
root.protocol('WM_DELETE_WINDOW', close)
root.resizable(False, False)

w = 376
h = 476

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()

x = (sw - w) / 2
y = (sh - h) / 2

client_name_lbl = ttk.Label(root, text="Имя:") # надписи и строки
client_name_lbl.place(x=10, y=10)

client_name_entry = ttk.Entry(root, width=59)
client_name_entry.place(x=10, y=30)

client_email_lbl = ttk.Label(root, text="Адрес e-mail:")
client_email_lbl.place(x=10, y=60)

client_email_entry = ttk.Entry(root, width=59)
client_email_entry.place(x=10, y=80)

client_address_lbl = ttk.Label(root, text="Адрес доставки:")
client_address_lbl.place(x=10, y=110)

client_address_entry = ttk.Entry(root, width=59)
client_address_entry.place(x=10, y=130)

client_phone_lbl = ttk.Label(root, text="Контактный телефон:")
client_phone_lbl.place(x=10, y=160)

client_phone_entry = ttk.Entry(root, width=59)
client_phone_entry.place(x=10, y=180)

client_prod_lbl = ttk.Label(root, text="ID продукта:")
client_prod_lbl.place(x=10, y=210)

client_prod_entry = ttk.Entry(root, width=59)
client_prod_entry.place(x=10, y=230)

client_info_lbl = ttk.Label(root, text="Подробная информация о заказе:")
client_info_lbl.place(x=10, y=260)

frame_info = ttk.Frame(root)
frame_info.place(x=10, y=280, height=100, width=355)

text_info = Text(frame_info, font='Arial 14', wrap=WORD)
text_info.pack(fill=BOTH)

client_capcha_lbl = ttk.Label(root, text="Число с картинки")
client_capcha_lbl.place(x=10, y=390)

client_capcha_entry = ttk.Entry(root, width=59)
client_capcha_entry.place(x=10, y=410)

button = ttk.Button(root,
                    text="Отправить",
                    command=button_clicked)
button.place(x=170, y=440)

captcha_img = ImageTk.PhotoImage(Image.open('captcha.png'))
captcha_label = Label(root, image=captcha_img)
captcha_label.place(x=10, y=440)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root.mainloop() # конец программы