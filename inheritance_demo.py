class person:
    name = ''
    age = 13
    address = ''
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
    def input_data(self):
        name = input('\n enter student\'s name:')
        age = int(input('\n Enter age of the student'))
        address = input('\n Enter the address: ')
    def display(self):
        print('Name: ',self.name)
        print('Age: ',self.age)
        print('Address: ',self.address)
class student(person):
    clas = 8
    school = ''
    mark = ''
    def display_detals(self):
        super().display()
        print('Class: ',self.clas)
        print('School: ',self.school)
        print('Mark : ',self.mark)
    def input_data_d(self):
        self.clas = int(input('Enter the class name: '))
        self.school = input('Enter the name of school: ')
        self.mark = int(input('Enter the marks : '))
p = person('Ambu',12,'Athira Nivas, Eravukadu')
p.display()

q = student('Lela',12,'Anizham Nivas Kalarkode')
q.display()

r = student('Kichu',14,'Indu Bhavan')
r.input_data_d()
r.display_detals()