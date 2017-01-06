from main import Main
from Person import Person
from Transaction import Transaction


class AppTester:

    def __init__(self):
        # TODO: this is sooo primitive. We should use some UT framework!
        self.all_tests = 0
        self.failed_tests = 0
        server = Main()

        for i in range(10):
            p = Person(i, "name_" + str(i), 1964 + i, "pass")
            server.register_new_customer(p)
        print(self.__class__.__name__ + " created")
# TODO: decide if these should e class/staticmethods or every test should
# be instance method

    def test_create_transaction_instance(self):
        self.all_tests += 1
        try:
            transaction = Transaction("Send Err", "Rec Iever",
                                      "100", "2016-01-01:20:19:45")
            print(transaction)
        except:
            self.failed_tests += 1
            print("Unexpected error:", sys.exc_info()[0])
            return False
        return True

    def run_tests(self):
        ''' put the desired tests here for smoke testing '''
        self.test_create_transaction_instance()
        print("All tests ran. Failed/All: {} / {}".format(self.failed_tests,
                                                          self.all_tests))

if __name__ == "__main__":
    AppTester().run_tests()
