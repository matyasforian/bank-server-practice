

class Main:

    def __init__(self):
        self.persons = []

    def register_new_customer(self, a_person):
        self.persons.append(a_person)

    def open_account(self, person_id):
        per = self.find_person(person_id)
        if per != None:
            per.open_account()
        else:
            print("open_account Error")

    def find_person(self, person_id):
        for per in self.persons:
            if person_id == per.id:
                return per
        return None

    def get_all_transactions(self):
        pass

if __name__ == "__main__":
    Main()