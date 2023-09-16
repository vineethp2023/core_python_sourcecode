class student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
    def getdetails(self):
        self.name = input("enter your name\n")
        self.mark = int(input("enter your mark\n"))
    def putdetails(self):
        print(' name: ',self.name,' mark : ',self.mark)
obj = student('','')
obj.getdetails()
obj.putdetails()
