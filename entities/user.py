class User:
    def __init__(self, name: str, pin: int, asset: float):  # asset will soon be Asset type
        assert 1000 <= pin <= 9999, f"Pin must have 4 numerical digits!"

        self.__name = name
        self.__pin = pin
        self.__asset = asset

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, value):
        self.__pin = value

    @property
    def asset(self):
        return self.__asset

    # Methods

    @staticmethod
    def register(file: str) -> None:
        """ Gets input of username and pin to put in
            user data file"""

        # loop to get username in the right way
        while True:
            try:
                print("Username:")
                username = input(">>> ")
                if not (5 <= len(username) <= 16):
                    raise Exception("Username must be from 5 to 16 characters!")
            except ValueError:
                print("Invalid value!")
                print("Try again...")
            except Exception as e:
                print(e)
            else:
                break

        # loop to get pin in the right way
        while True:
            try:
                print("Pin:")
                pin = int(input(">>> "))
                if not (1000 <= pin <= 9999):
                    raise Exception("Pin must have 4 digits!")
            except ValueError:
                print("Invalid value!")
                print("Try again...")
            except Exception as e:
                print(e)
            else:
                break

        with open(file, 'a') as f:
            f.write(f"{username}:{pin}\n")

    @staticmethod
    def login():
        pass
