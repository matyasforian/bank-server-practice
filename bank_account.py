

class BankAccount:

    account_counter = 0

    def __init__(self):
        self.balance = 0
        self.account_number = self.account_number_generator()

    @classmethod
    def account_number_generator(cls):
        base_number = 1000 + cls.account_counter
        cls.account_counter += 1
        return base_number
