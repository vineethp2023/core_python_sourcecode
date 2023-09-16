class person:
    def getdata(self):
        self.name = input("Enter the name : ")
        self.age = int(input("\nEnter the mark: "))
        self.dob = input("\n Enter the date of birth: ")
        self.course  = input("\n Enter the course name: ")
    def __init__(self,name,mark,dob,course):
        self.name = name
        self.mark = mark
        self.dob = dob
        self.course = course
    def display(self):
        print('Name : ',self.name)
        print('Mark : ',self.mark)
        print('Date of Birth: ',self.dob)
        print('Course Name: ',self.course)
p = person('Vineeth P',250,'2000-aug-03','MCA')
p.display()
q = person('Afueth Thomas',280,'1999-12-19','Msc')
q.getdata()
q.display()