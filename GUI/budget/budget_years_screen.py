from services.account_service import AccountService as AcS
from GUI.screen import *
from entities.user import *


class BudgetYearsScreen(Screen):
    def __init__(self):
        super().__init__(title="Budget")

        # Page main frame
        self.__frame = LabelFrame(self.root, text="Budget Years")
        self.__frame.pack()

        # Options widget
        clicked = StringVar()
        clicked.set("2022")

        self.__options = OptionMenu(self.__frame, clicked, "2022", "2023", "2024")
        self.__options.pack()

        # Confirm Button
        self.__button_confirm = Button(self.__frame, text="Confirm", command=lambda: [])
        self.__button_confirm.pack()
