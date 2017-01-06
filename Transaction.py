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
