class patients:
    def __init__(self, name, age, date_of_latest_admission, medical_history):
        self.name = name
        self.age = age
        self.date_of_latest_admission = date_of_latest_admission
        self.medical_history = medical_history
    def print_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Date of Admission: {self.date_of_latest_admission}, Medical History: {self.medical_history}")
name = input("enter the name")
age = input("enter the age")
date_of_latest_admission = input("enter the date_of_latest_admission")
wmedical_history = input("enter the medical_history")
patient1 = patients(name,age,date_of_latest_admission,wmedical_history)
patient1.print_details()