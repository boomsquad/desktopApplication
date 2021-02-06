from tkinter import *


master = Tk()
master.title('Desktop Application')
master.geometry("300x400")


class Username:
    usernameLabel = Label(master, text="username").grid(row=1, column=0)
    usernameTextbox = Entry(master, width=30).grid(row=1, column=1)


class Password:
    passwordLabel = Label(master, text="password").grid(row=2, column=0)
    passwordTextbox = Entry(master, show="*", width=30).grid(row=2, column=1)


def login():
    read = Label(master, text="username is " + Username.usernameTextbox.get() +
                              " password is " + Password.passwordTextbox.get())
    read.pack()


passwordCheckbox = IntVar()


def reveal():
    if passwordCheckbox.get() == 1:
        save = Password.passwordTextbox.get()
        Password.passwordTextbox = Entry(master, text=save, width=30).grid(row=2, column=1)

    elif passwordCheckbox.get() == 0:
        Password.passwordTextbox = Entry(master, show="*", width=30).grid(row=2, column=1)


checkButton = Checkbutton(master, text="show password", variable=passwordCheckbox, onvalue=1, offvalue=0,
                          command=reveal).grid(column=1)
loginButton = Button(master, text="Login", command=login).grid(column=1, pady=4)


mainloop()
