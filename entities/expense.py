class Expense:

    def __init__(self, name: str, category, money_amount: float, date, payment_method, sub_category=None):

        # Assert
        assert money_amount > 0, "money_amount must be greater than 0"

        # Assign
        self.__name = name
        self.__category = category
        self.__money_amount = money_amount
        self.__date = date
        self.__payment_method = payment_method
        self.__sub_category = sub_category

    # Getters and Setters
    @property
    def name(self):
        return self.__name

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        self.__category = value

    @property
    def money_amount(self):
        return self.__money_amount

    @property
    def date(self):
        return self.__date

    @property
    def payment_method(self):
        return self.__payment_method

    @property
    def sub_category(self):
        return self.__sub_category

    @sub_category.setter
    def sub_category(self, value):
        self.__sub_category = value
