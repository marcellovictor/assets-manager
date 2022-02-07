"""
This class is probably going to be deleted
"""

from tkinter import *
from services.account_service import AccountService as AcS
from GUI.screen import *
from entities.user import *


class InitialScreen(Screen):
    def __init__(self):
        super().__init__(title="Login/Register")

        # Page main frame
        self.__frame = LabelFrame(self.root, text="InitalScreen")
        self.__frame.pack()

        # Welcome Label
        self.__label_welcome = Label(self.__frame, text="Welcome", padx=200)
        self.__label_welcome.grid(row=0, column=1)

        # Username
        self.__label_username = Label(self.__frame, text="username: ")
        self.__label_username.grid(row=1, column=0)

        self.__input_username = Entry(self.__frame)
        self.__input_username.grid(row=1, column=1)

        # Pin
        self.__label_pin = Label(self.__frame, text="pin: ")
        self.__label_pin.grid(row=2, column=0)

        self.__input_pin = Entry(self.__frame)
        self.__input_pin.grid(row=2, column=1)

        # Login button
        self.__button_login = Button(self.__frame, text="Login")
        self.__button_login.grid(row=3, column=1)

        # Loop //-----//-----//
        self.root.mainloop()

    """   
    @property
    def frame(self):
        return self.__frame
    
    @property
    def label_welcome(self):
        return self.__label_welcome
    
    @property
    def label_username(self):
        return self.__label_username
    
    @property
    def input_username(self):
        return self.__input_username
    
    @property
    def label_pin(self):
        return self.__label_pin
    
    @property
    def input_pin(self):
        return self.__input_pin
    
    @property
    def button_login(self):
        return self.__button_login
    """

    def button_login_clicked(self):
        user = AcS.login(self.__input_username.get(), int(self.__input_pin.get()))
        if type(user) == User:
            return user
        else:
            pass
            # TODO janelinha de erro que diz invalid data








"""
root = Tk()
root.geometry("800x600+350+100")

# Variables
user = None
login_tried = False

# Page main frame
frame = LabelFrame(root, text="InitalScreen")
frame.pack()

# Welcome Label
label_welcome = Label(frame, text="Welcome", padx=200)
label_welcome.grid(row=0, column=1)

# Username
label_username = Label(frame, text="username: ")
label_username.grid(row=1, column=0)

input_username = Entry(frame)
input_username.grid(row=1, column=1)

# Pin
label_pin = Label(frame, text="pin: ")
label_pin.grid(row=2, column=0)

input_pin = Entry(frame)
input_pin.grid(row=2, column=1)

# Login button
button_login = Button(frame, text="Login", command=)
button_login.grid(row=3, column=1)

if login_tried:
    user = AcS.login(username=input_username.get(), pin=int(input_pin.get()))

"""