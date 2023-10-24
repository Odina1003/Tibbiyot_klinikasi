from shifokor import Shifokor

class Doctor:
    def __init__(self):
        self._doctor_list: list[Shifokor] = []

    def add_doctor(self, ism, familiya, ssn, id, mutaxassisligi):
        shifokor = Shifokor(ism, familiya, ssn, id, mutaxassisligi)
        self._doctor_list.append(shifokor)
        print("Shifokor kiritildi")

    def get_doctor(self, id):
        for doctor in self._doctor_list:
            if doctor.id == id:
                return doctor
            
        return "NoSuchDoctor"
