class teacher:
    def __init__(self,id,name,dept,subject):
        self.id = id
        self.name = name
        self.dept = dept
        self.subject  = subject
    def get_details(self):
        self.id = int(input('\nEnter the id '))
        self.name = input('Enter the name: ')
        self.dept = input('Enter the name of department: ')
        self.subject = input('Enter the name of subject : ')
    def print_details(self):
        print('Teacher\'s information')
        print('ID........: ',self.id)
        print('NAME......: ',self.name)
        print('DEPARTMENT: ',self.dept)
        print('SUBJECT...: ',self.subject)
t = teacher('101','Sulochana','Computer Applications','Digital Electronics')
t2 = teacher('102','Kamala','Physics','Statics')
print('Detals of teacher 1\n')
t.print_details()
print('\n Details of teacher 2\n')
t2.print_details()
t3 = teacher('','','','')
t3.get_details()
print('Details of third teacher \n')
t3.print_details()


