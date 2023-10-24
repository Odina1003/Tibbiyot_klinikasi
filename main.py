from clinic import Clinic
from doctor import Doctor

clinic = Clinic()

clinic.add_patient("Xilola", "Umarova", 1)
print(clinic.get_patient(1))
print(clinic.get_patient(2))

doctor1 = Doctor()
doctor1.add_doctor("Ziyoda", "Karimova", 123, 43, "Stomatolog")
print(doctor1.get_doctor(43))
print(doctor1.get_doctor(45))