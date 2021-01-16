from tkinter import *
from tkinter import messagebox
import pickle
from random import randint



root = Tk()
root.geometry("300x500")
root.title("Войти в систему")



def registation():
    text= Label(text = "Для входа в систему заристируйтесь")
    text_login = Label(text = "Введите логин:")
    registation_login = Entry()
    text_password1 = Label(text = "Введите пароль:")
    registation_password1 = Entry(show = "*")
    text_password2 = Label(text="Повторите пароль:")
    registation_password2 = Entry(show = "*")
    button_registration = Button(text = "Зарегистироваться", command = lambda: save())
    text.pack()
    text_login.pack()
    registation_login.pack()
    text_password1.pack()
    registation_password1.pack()
    text_password2.pack()
    registation_password2.pack()
    button_registration.pack()

    def save():
        login_password_save = {}
        login_password_save [registation_login.get()] = registation_password1.get()
        doc = open("login.txt", "wb")
        pickle.dump(login_password_save, doc)
        doc.close()
        login()


def login():
    text_login = Label(text = "Теперь вы можете войти в систему")
    text_enter_login = Label(text = "Введите ваш логин")
    enter_login = Entry()
    text_enter_password = Label(text = "Введите ваш пароль")
    enter_password = Entry(show = "*")
    button_enter = Button(text = "Войти", command = lambda : login_pass())
    text_login.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_login.pack()
    text_enter_password.pack()
    enter_password.pack()
    button_enter.pack()

    def login_pass():
        doc = open("login.txt", "rb")
        a = pickle.load(doc)
        doc.close()
        if enter_login.get() in a:
            if enter_password.get() == a[enter_login.get()]:
                messagebox.showinfo("Вход выполнен", "Привет! У тебя 5 новых сообщений")
            else:
                messagebox.showerror("Ошибка", "Неверный пароль")
        else:
            messagebox.showerror("Ошибка", "Неверный логин")



registation()

root.mainloop()

