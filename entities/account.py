from entities.expense import Expense
from entities.income import Income


class Account:

    def __init__(self, acc_id: int, owner: str, balance=0.0):

        # Assert

        # Assign
        self.__acc_id = acc_id
        self.__owner = owner
        self.__balance = balance

        # List of Expenses
        self.__expenses_list = []
        """
        In the future, it will be necessary to initiate the list and load the data
        from the database to it. (also for the incomes list)
        """

        # List of Incomes
        self.__incomes_list = []

        # History List
        self.__history_list = []

    # Getters and Setters
    @property
    def acc_id(self):
        return self.__acc_id

    @property
    def owner(self):
        return self.__owner

    @property
    def balance(self):
        return self.__balance

    @property
    def expenses_list(self):
        return self.__expenses_list

    @property
    def incomes_list(self):
        return self.__incomes_list

    # Methods

    def __initiate_expenses_list(self):
        pass

    def __initiate_incomes_list(self):
        pass

    def register_expense(self, expense: Expense):
        try:
            self.__expenses_list.append(expense)
            self.__history_list.append(expense)
        except Exception as e:
            print("Erro:", e)
        else:
            self.__balance -= expense.money_amount

    def register_income(self, income: Income):
        try:
            self.__incomes_list.append(income)
            self.__history_list.append(income)
        except Exception as e:
            print("Erro:", e)
        else:
            self.__balance += income.money_amount
