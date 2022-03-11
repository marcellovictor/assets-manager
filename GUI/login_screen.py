"""
This class is probably going to be deleted
"""
import tkinter
from tkinter import *
from services.account_service import AccountService as AcS
from GUI.screen import *
from entities.user import *
from GUI.main_menu_screen import *
from PIL import ImageTk, Image


class LoginScreen(Screen):
    def __init__(self):
        super().__init__(title="Login")

        # Page Settings
        self.root.configure(bg='#65A8E1')

        """
        Down here I use a background image as base to put
        widgets in its' right places
        """

        bg_image = ImageTk.PhotoImage(Image.open('imgs\\LoginScreen.jpg'))
        bg_label = Label(self.root, image=bg_image)
        bg_label.place(x=0, y=0)

        # Welcome Label
        self.__label_welcome = Label(self.root, text="Welcome", padx=200)
        # self.__label_welcome.grid(row=0, column=1)
        self.__label_welcome.place(x=180, y=30)

        # Username
        self.__label_username = Label(self.root, text="username: ")
        self.__label_username.place(x=240, y=285)

        self.__input_username = Entry(self.root)
        self.__input_username.place(x=320, y=285)

        # Pin
        self.__label_pin = Label(self.root, text="pin: ")
        self.__label_pin.place(x=240, y=340)

        self.__input_pin = Entry(self.root)
        self.__input_pin.place(x=320, y=340)

        # Login button
        self.__button_login = Button(self.root, text="Login", command=lambda: [self.root.destroy(), MainMenuScreen()])
        self.__button_login.place(x=370, y=410)

        # Loop //-----//-----//
        self.root.mainloop()


    """
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
        self.root.destroy()
        MainMenuScreen()

        """user = AcS.login(self.__input_username.get(), int(self.__input_pin.get()))
        if type(user) == User:
            return user
        else:
            pass
            # TODO janelinha de erro que diz invalid data"""








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