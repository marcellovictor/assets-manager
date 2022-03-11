from GUI.budget.budget_years_screen import *


class MainMenuScreen(Screen):
    def __init__(self):
        super().__init__(title="Main Menu")

        # Page main frame
        self.__frame = LabelFrame(self.root, text="Main Menu")
        self.__frame.pack()

        # Welcome Label
        self.__label_welcome = Label(self.__frame, text="Welcome", padx=200)
        self.__label_welcome.grid(row=0, column=1)

        # Budget Button
        self.__button_budget = Button(self.__frame, text="Budget", command=lambda: [self.root.destroy(), BudgetYearsScreen()])
        self.__button_budget.grid(row=2, column=0)

        # Investments Button
        self.__button_budget = Button(self.__frame, text="Investments")
        self.__button_budget.grid(row=2, column=2)

        # Treasure Button
        self.__button_budget = Button(self.__frame, text="Asset")
        self.__button_budget.grid(row=3, column=1)
