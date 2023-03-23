from expense import Expense


class Subscription(Expense):
    def __init__(self, name: str, category, money_amount: float, date, payment_method):
        super().__init__(name, category, money_amount, date, payment_method)
