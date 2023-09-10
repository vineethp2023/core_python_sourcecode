class GrandFather:
    def __init__(self,name,age):
        self.name  = name
        self.age = age
    def print_details(self):
        print('NAME : ',self.name,'AGE : ',self.age)
class Father(GrandFather):
    def __init__(self,name,age,name1,age1):
        super().__init__(name,age)
        self.father_name = name1
        self.father_age = age1
    def print_details(self):
        print('NAME : ',self.father_name,'AGE : ',self.father_age)
        print('FATHER\'S NAME : ',self.name,'FATHER\'S AGE: ',self.age)
class Child(Father):
    def get_details(self):
        self.name_c = input('Enter your name: ')
        self.age_c = int(input('Enter your age: '))
        self.clas = input('Enter your class: ')
        self.school = input('Enter your school name: ')
        self.adddress = input('Enter your address: ')
        self.phone = input('Enter your phone number ')
    def display_bio(self):
        print('BIO DATA OF ',self.name_c)
        print('\n-------------------------\n')
        print('NAME.........:',self.name_c)
        print('AGE..........:',self.age_c)
        print('STANDARD.....:',self.clas)
        print('SCHOOL.......:',self.school)
        print('ADDRESS......:',self.adddress)
        print('PHONE NO.....:',self.phone)
        print('FATHER.......:',self.father_name)
        print('FATHER\'S AGE:',self.father_age)
        print('GRAND FATHER.:',self.name)
        print('GRAND.F\'s AGE: ',self.age)
        print('**----End of report----**')
cob = Child('Soolapani S',80,'Pradeep S',50)
cob.get_details()
cob.display_bio()