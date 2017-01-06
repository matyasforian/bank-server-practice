from main import Main
from Person import Person

class AppTester:

    def __init__(self):
        server = Main()

        for i in range(10):
            p = Person(i, "name_" + str(i), 1964 + i, "pass")
            server.register_new_customer(p)

        
        print("done")

AppTester()
