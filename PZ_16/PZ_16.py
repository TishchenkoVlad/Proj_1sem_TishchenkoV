#Приложение ПРОКАТ АВТОМОБИЛЕЙ для некоторой организации. БД должна
#содержать таблицу Клиент со следующей структурой записи: ФИО клиента, марка авто,
#срок проката, сумма, предоплата (да/нет).
#БД должна обеспечивать получение информации по сумме.


import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):

    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#6EADDC', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="plus.png")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить клиента', command=self.open_dialog, bg='#836BE4', bd=1,
                                    compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file="molot.png")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#836BE4',
                                    bd=1, compound=tk.TOP, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="del.png")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#836BE4',
                                    bd=1, compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="poisk.png")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#836BE4',
                               bd=1, compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="ob.png")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#836BE4',
                               bd=1, compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('fio', 'avto', 'time', 'sum', 'pred'), height=15, show='headings')

        self.tree.column('fio', width=50, anchor=tk.CENTER)
        self.tree.column('avto', width=180, anchor=tk.CENTER)
        self.tree.column('time', width=140, anchor=tk.CENTER)
        self.tree.column('sum', width=140, anchor=tk.CENTER)
        self.tree.column('pred', width=140, anchor=tk.CENTER)

        self.tree.heading('fio', text='ФИО')
        self.tree.heading('avto', text='Марка авто')
        self.tree.heading('time', text='Срок проката')
        self.tree.heading('sum', text='Сумма')
        self.tree.heading('pred', text='Предоплата')

        self.tree.pack()

    def records(self, fio, avto, time, sum, pred):
        self.db.insert_data(fio, avto, time, sum, pred)
        self.view_records()

    def update_record(self, fio, avto, time, sum, pred):
        self.db.cur.execute("""UPDATE users SET fio=?, avto=?, time=?, sum=?, pred=? WHERE fio=?""",
                            (fio, avto, time, sum, pred, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM users""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM users WHERE fio=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    # def search_records(self, user_id):
    #     user_id = ("%" + user_id + "%",)
    #     self.db.cur.execute("""SELECT * FROM users WHERE name LIKE ?""", user_id)
    #     [self.tree.delete(i) for i in self.tree.get_children()]
    #     [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def search_records(self, sum):
        sum = (sum,)
        self.db.cur.execute("""SELECT * FROM users WHERE sum>=?""", sum)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]


    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()

class Child(tk.Toplevel):

    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.iconphoto(False, tk.PhotoImage(file='icon.png'))
        self.title('Добавить клиента')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_fio = tk.Label(self, text='ФИО')
        label_fio.place(x=50, y=25)
        self.entry_fio = ttk.Entry(self)
        self.entry_fio.place(x=110, y=25)

        label_avto = tk.Label(self, text='Марка авто')
        label_avto.place(x=40, y=50)
        self.entry_avto = ttk.Entry(self)
        self.entry_avto.place(x=110, y=50)

        label_time = tk.Label(self, text='Срок проката')
        label_time.place(x=30, y=75)
        self.entry_time = ttk.Entry(self)
        self.entry_time.place(x=110, y=75)

        label_sum = tk.Label(self, text='Сумма')
        label_sum.place(x=50, y=100)
        self.entry_sum = ttk.Entry(self)
        self.entry_sum.place(x=110, y=100)

        label_pred = tk.Label(self, text='Предоплата')
        label_pred.place(x=35, y=125)
        self.combobox_pred = ttk.Combobox(self, values=[u'Да', u'Нет'])
        self.combobox_pred.current(0)
        self.combobox_pred.place(x=110, y=125)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_fio.get(),
                                                                       self.entry_avto.get(),
                                                                       self.entry_time.get(),
                                                                       self.entry_sum.get(),
                                                                       self.combobox_pred.get()
                                                                       ))

        self.grab_set()
        self.focus_set()

class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=170)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_fio.get(),
                                                                          self.entry_avto.get(),
                                                                          self.entry_time.get(),
                                                                          self.entry_sum.get(),
                                                                          self.combobox_pred.get()))
        self.btn_ok.destroy()

class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.iconphoto(False, tk.PhotoImage(file='icon.png'))
        self.title("Поиск")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск")
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

class DB:
    def __init__(self):

        with sq.connect('BD/saper.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
                fio TEXT,
                avto TEXT NOT NULL,
                time INTEGER,
                sum INTEGER,
                pred INTEGER NOT NULL DEFAULT 1
                )""")

    def insert_data(self, fio, avto, time, sum, pred):
        self.cur.execute("""INSERT INTO users(fio, avto, time, sum, pred) VALUES (?, ?, ?, ?, ?)""",
                             (fio, avto, time, sum, pred))
        self.con.commit()

if __name__ == "__main__":
    root = tk.Tk()
    root.iconphoto(False, tk.PhotoImage(file='icon.png'))
    db = DB()
    app = Main(root)
    app.pack()
    root.title("ПРОКАТ АВТОМОБИЛЕЙ")
    root.geometry("900x400")
    root.resizable(False, False)
    root.mainloop()