list1 = [1,2,'python',"Java",'C++', "C#"]
print(list1)
print('0th:',list1[0])
print('1st:',list1[1])
print('2nd:',list1[2])
print('length of the list: ',len(list1))
print('Data type of list: ',type(list1))
list2 = list(('Apple', "Banana", "Orange", "Mango", 'Plum'))
print('Another list of fruits is\n',list2)
print('first item: ',list2[0])
print('Second item: ',list2[1])
print('Combining both lists\n',list1+list2)
list3 = [10,20,'30',40,'50']
print(list3[0]+3)
print(list3[1]+3)
print(int(list3[2])+5)
print('List appending example\n')
print('List 2 is the list of fruits\n')
print(list2)
print('Appending pineapple to list2\n')
list2.append('Pineapple')
print('Again printing list of fruits\n')
print(list2)
print(list2.index('Plum'))
