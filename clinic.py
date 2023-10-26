from person import Person
from doctor import Doctor

class Clinic:
    def __init__(self):
        self._bemor: list[Person] = []
        self._doctor_list: list[Doctor] = []

    def add_patient(self, name, familiya, ssn):
        info = Person(name, familiya, ssn)
        self._bemor.append(info)
        print("Bemor ro'yhatga kiritildi")

    def get_patient(self, id):
        for person in self._bemor:
            if person.ssn == id:
                return person
            
        return "NoSuchPatient"
    
    def add_doctor(self, ism, familiya, ssn, id, mutaxassisligi):
        shifokor = Doctor(ism, familiya, ssn, id, mutaxassisligi)
        self._doctor_list.append(shifokor)
        print("Shifokor kiritildi")

    def get_doctor(self, id):
        for doctor in self._doctor_list:
            if doctor.id == id:
                return doctor
            
        return "NoSuchDoctor"

    def assign_patient_to_doctor(self, ssn, id):
        try:
            doctor = self.get_doctor(id)
        except:
            raise "NoSuchDoctor"(id)
        try:
            patient = self.get_patient(ssn)
        except:
            raise "NoSuchPatient"(ssn)
        doctor.attach_patient(ssn)
        patient.set_doctor(id)

    def idle_doctor(self):
        list1 = []
        for shifokor in self._doctor_list:
            if shifokor._patient_list == None:
                list1.append(shifokor)
        return list1
    
    def busy_doctors(self):
        list2 = []
        for shifokor in self._doctor_list:
            if shifokor._patient_list != None:
                list2.append(shifokor)
        return list2
    
    def doctors_by_num_patients(self, doctor):
        count = 0
        for i in self._doctor_list:
            if i.ism == doctor:
                for j in self._bemor:
                    count += 1
        return f"{count}: {j.ssn} {j.familiya} {j.ism}"
    
    def count_patients_per_specialization(self):
        pass