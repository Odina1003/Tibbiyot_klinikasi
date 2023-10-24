from person import Person

class Clinic:
    def __init__(self):
        self._bemor: list[Person] = []

    def add_patient(self, name, familiya, ssn):
        info = Person(name, familiya, ssn)
        self._bemor.append(info)
        print("Bemor ro'yhatga kiritildi")

    def get_patient(self, id):
        for person in self._bemor:
            if person.ssn == id:
                return person
            
        return "NoSuchPatient"
    