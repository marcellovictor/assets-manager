from entities.account import Account


def print_menu():
    print(f"{' Main Menu ':#^40}")
    print()
    print(f"{'0. Leave App'}")
    print(f"{'1. Check Balance'}")
    print(f"{'2. Register Expense'}")
    print(f"{'3. Register Income'}")
    print(f"{'4. Account History'}")
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


if __name__ == '__main__':

    account = Account(1234, "Fulano")

    while True:
        print_menu()

        option = int(input(">>>  "))

        if option == 0:
            break
        elif option == 1:
            pass
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            pass
        else:
            print("Invalid Value!")
            print(f"Valid inputs are integers from {0} to {4}.")

    print("Leaving...")
