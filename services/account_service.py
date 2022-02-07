from entities.user import User


class AccountService:

    accounts_file = "data/users.txt"

    @classmethod
    def register(cls, username: str, pin: int) -> User:
        """
        Gets username and pin to put in
        user data file
        """

        # loop to get username in the right way

        try:
            if not (5 <= len(username) <= 16):
                raise Exception("Username must be from 5 to 16 characters!")
        except ValueError:
            print("Invalid value!")
            print("Try again...")
        except Exception as e:
            print(e)

        # loop to get pin in the right way
        try:
            if not len(str(pin)) == 4:
                raise Exception("Pin must have 4 digits!")
        except ValueError:
            print("Invalid value!")
            print("Try again...")
        except Exception as e:
            print(e)

        with open(cls.accounts_file, 'a') as f:
            f.write(f"{username}:{pin}\n")

        return User(username, pin, 0.0)

    @classmethod
    def login(cls, username: str, pin: int) -> User:
        """
        Goes through the file searching for the username
        and checks if it exists.

        If it does, checks if the pin is right.
        """

        username_check = False
        pin_check = False

        file_username = ''
        file_pin = -1

        try:
            # Iterate file lines to find account asked
            with open(cls.accounts_file, 'r') as f:
                for line in f:
                    acc_data = line.split(':')
                    current_username = acc_data[0]
                    current_pin = acc_data[1]

                    if current_username == username:
                        file_username = current_username
                        file_pin = int(current_pin)

                        username_check = True

                        break

            # First step of checking (username)
            if not username_check:
                raise Exception("Username not found!")

            # Second step of checking (pin)
            pin_check = (file_pin == pin)

            if not pin_check:
                raise Exception("Pin invalid!")
        except Exception as e:
            print(e)
            return None

        return User(username, pin, 0.0)
