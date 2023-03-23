class Account:

    def __init__(self, acc_id: int, owner: str, balance=0.0):

        # Assert

        # Assign
        self.__acc_id = acc_id
        self.__owner = owner
        self.__balance = balance

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
