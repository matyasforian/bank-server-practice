from bank_account import BankAccount

class Person:

    def __init__(self, id, name, birth_date, password):
        self.id = id
        self.name = name
        self.birth_date = birth_date
        self.password = password
        self.bank_accounts = []

    def open_account(self):
        new_acc = BankAccount()
        self.bank_accounts.append(new_acc)
