marklist = {'Vineeth':95,'Rahul':93,'Vinay':93,'Rohit':95,'Pavithra':90,'Sooraj':91,'Kiran':90,'Abhijith':95,'Ananya':97}
print('Marklist of the students:\n',marklist)
print('Creating a custom dictionary\n')
print('How many students in the class ?')
n = int(input())
mark_details = {}
for i in range(n):
    print('Enter the name of student ',i+1,': ')
    name = input()
    print('Enter the mark of ',name,': ')
    mark = int(input())
    mark_details.update({name:mark})
print('Mark list of ',n,' students\n')
print(mark_details)


