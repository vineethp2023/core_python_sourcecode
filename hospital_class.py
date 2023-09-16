class hospital:
    def __init__(self,admin,doctor,dept,sister):
        self.admin = admin
        self.doctor = doctor
        self.dept = dept
        self.sister = sister
class department(hospital):
    def __init__(self,admin,doctor,dept,sister,timing,date,fee):
        super().__init__(admin,doctor,dept,sister)
        self.timing = timing
        self.date = date
        self.fee = fee
class patientward(department):
    def __init__(self,name,age,disease,admin,doctor,dept,sister,timing,date,fee):
        super().__init__(admin,doctor,dept,sister,timing,date,fee)
        self.name = name
        self.age = age
        self.disease = disease
    def print_details(self):
        print('Patient information')
        print('\n------------------\n')
        print('NAME.....: ',self.name)
        print('AGE......',self.age)
        print('DOCTOR...',self.doctor)
        print('NURSE....',self.sister)
        print('DEPARTMENT....',self.dept)
        print('DATE OF CONSULTATION: ',self.date)
        print('TIME SLOT ALLOTED: ',self.timing)
        print('DISEASE TYPE: ',self.disease)
patient = patientward('Akash S',29,'Troat Infection','Philip K S','Dr. Prakash M','ENT department','Sr.Lakshmi','10.30 AM','21-June-2023','100 Rs')
patient.print_details()
