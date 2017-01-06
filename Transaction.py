class Transaction:

    def __init__(self, sender, receiver, amount, date_time):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.date_time = date_time

    def __str__(self):
        return "sender: {}\nreceiver: {}\namount: {}\ndate/time: {}".format(self.sender,
                                                                            self.receiver,
                                                                            self.amount,
                                                                            self.date_time)

    def __repr__(self):
        return self.__str__()

# tests
# TODO: remove these and put to the main tester file


def test_print_transaction():
    transaction = Transaction("Send Err", "Rec Iever",
                              "100", "2016-01-01:20:19:45")
    print(transaction)

if __name__ == "__main__":
    test_print_transaction()
