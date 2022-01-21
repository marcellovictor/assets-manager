from entities.user import User
from services.account_service import AccountService

print("==============")
print("Sign in (S)")
print("Register (R)")
print("==============")

print()
command = input(">>> ").strip().upper()

if command == 'S':  # login
    while True:
        print()
        print("Username:")
        username = input(">>> ").strip()

        print()
        print("Pin:")
        pin = int(input(">>> "))

        result = AccountService.login(username, pin)

        if result:
            break
        else:
            print("Try again...")

    print()
    print("Logged successfully!")
    print()

elif command == 'R':  # register
    # username input
    while True:
        print()
        print("Username:")
        username = input(">>> ").strip()

        if 5 <= len(username) <= 16:
            break
        else:
            print("-----------------------------------------")
            print("Username must be from 5 to 16 characters!")
            print("-----------------------------------------")

    # pin input
    while True:
        print()
        print("Pin:")
        pin = int(input(">>> ").strip())

        if len(str(pin)) == 4:
            break
        else:
            print("-----------------------")
            print("Pin must have 4 digits!")
            print("-----------------------")

    AccountService.register(username, pin)
    print()
    print("Account registered successfully!")
    print()
