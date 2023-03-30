from entities.account import Account
from entities.expense import Expense
from entities.income import Income


def print_menu():
    print(f"{' Main Menu ':#^40}")
    print()
    print(f"{'0. Leave App'}")
    print(f"{'1. Check Balance'}")
    print(f"{'2. Register Expense'}")
    print(f"{'3. Register Income'}")
    print(f"{'4. Account History'}")
    print()


def print_balance(account: Account):
    print()
    print("==//=="*6)
    print()
    print(f"{account.owner}'s Balance: R${account.balance:.2f}")
    print()
    print("==//==" * 6)
    print()


def menu_option_choice(a: int, b: int) -> int:  # just a function to test docstrings, will be removed later
    """
    Receive an input from user, validate and return it when valid.
    Value must be an integer between parameters "a" and "b".

    :argument a: initial range value
    :argument b: final range value
    :return: option chosen by the user
    """
    while True:
        try:
            value = int(input(">>>  "))
            if value < a or value > b:
                raise ValueError
            return value
        except ValueError:
            print()
            print("Invalid Value!")
            print(f"Valid inputs are integers from {a} to {b}.")
            print()


def instance_expense():  # return expense
    try:
        name = input("Name: ")
        category = input("Category: ")
        money_amount = float(input("Value: "))
        date = input("Date: ")
        payment_method = input("Payment Method: ")

        expense = Expense(name, category, money_amount, date, payment_method)
        return expense
    except ValueError as ve:
        print(ve)


def instance_income():  # return income
    try:
        name = input("Name: ")
        money_amount = float(input("Value: "))
        date = input("Date: ")

        income = Income(name, money_amount, date)
        return income
    except ValueError as ve:
        print(ve)


if __name__ == '__main__':

    fulano_account = Account(1234, "Fulano")

    while True:
        print_menu()

        option = int(input(">>>  "))

        if option == 0:  # Leave app
            break
        elif option == 1:
            print_balance(fulano_account)
        elif option == 2:  # Register Expense
            try:
                expense = instance_expense()
            except Exception as e:
                print("Error instanciating the expense:", e)
            else:
                try:
                    fulano_account.register_expense(expense)
                except Exception as e:
                    print("Error registering the expense:", e)
        elif option == 3:  # Register Income
            try:
                income = instance_income()
            except Exception as e:
                print("Error instanciating the income:", e)
            else:
                try:
                    fulano_account.register_income(income)
                except Exception as e:
                    print("Error registering the expense:", e)
        elif option == 4:  # Check Account History
            pass
        else:
            print("Invalid Value!")
            print(f"Valid inputs are integers from {0} to {4}.")

    print("Leaving...")
