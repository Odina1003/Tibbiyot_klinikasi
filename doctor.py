from person import Person

class Doctor:
    def __init__(self, ism, familiya, ssn, id, mutaxassisligi):
        self._ism = ism
        self._familiya = familiya
        self._ssn = ssn
        self._id = id
        self._mutaxassisligi = mutaxassisligi
        self._patient_list: list[Person] = []

    @property
    def ism(self):
        return self._ism
    
    @property
    def familiya(self):
        return self._familiya
    
    @property
    def ssn(self):
        return self._ssn
    
    @property
    def id(self):
        return self._id
       
    @property
    def mutaxassisligi(self):
        return self._mutaxassisligi
    
    def attach_patient(self, patients):
        attach = self._patient_list.append(patients)

    def __str__(self):
        return f"Shifokor Ismi:{self.ism}, Familiyasi:{self.familiya}, SSN:{self.ssn}, ID:{self.id}, Mutaxassisligi:{self.mutaxassisligi}"