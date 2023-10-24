class Shifokor:
    def __init__(self, ism, familiya, ssn, id, mutaxassisligi):
        self._ism = ism
        self._familiya = familiya
        self._ssn = ssn
        self._id = id
        self._mutaxassisligi = mutaxassisligi

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
    
    def __str__(self):
        return f"Shifokor Ismi:{self.ism}, Familiyasi:{self.familiya}, SSN:{self.ssn}, ID:{self.id}, Mutaxassisligi:{self.mutaxassisligi}"