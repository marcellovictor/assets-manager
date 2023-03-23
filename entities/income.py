class Income:

    def __init__(self, name: str, money_amount: float, date):

        # Assert
        assert money_amount > 0, "money_amount must be greater than 0"

        # Assign
        self.__name = name
        self.__money_amount = money_amount
        self.__date = date

    # Getters and Setters
    @property
    def name(self):
        return self.__name

    @property
    def money_amount(self):
        return self.__money_amount

    @property
    def date(self):
        return self.__date
