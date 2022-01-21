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
