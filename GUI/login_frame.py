from tkinter import *


class LoginFrame(LabelFrame):
    def __init__(self, root: Tk):
        super().__init__(root, text="Login")

        # Welcome Label
        self.__label_welcome = Label(self, text="Welcome", padx=200)
        self.__label_welcome.grid(row=0, column=1)

        # Username
        self.__label_username = Label(self, text="username: ")
        self.__label_username.grid(row=1, column=0)

        self.__input_username = Entry(self)
        self.__input_username.grid(row=1, column=1)

        # Pin
        self.__label_pin = Label(self, text="pin: ")
        self.__label_pin.grid(row=2, column=0)

        self.__input_pin = Entry(self)
        self.__input_pin.grid(row=2, column=1)

        # Login button
        self.__button_login = Button(self, text="Login")
        self.__button_login.grid(row=3, column=1)
