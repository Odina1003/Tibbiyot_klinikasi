class Person:
    def __init__(self, ism, familiya, ssn):
        self._ism = ism
        self._familiya = familiya
        self._ssn = ssn

    @property
    def ism(self):
        return self._ism
    
    @property
    def familiya(self):
        return self._familiya
    
    @property
    def ssn(self):
        return self._ssn
    
    def __str__(self):
        return f"Bemorning Ismi: {self.ism}, Familiyasi: {self.familiya}, SSN: {self.ssn}"