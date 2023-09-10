list1 = list((1,2,3,4,5,6,7,8,9,10))
print(list1)
print(list1[1:])
print(list1[2:5])
print(list1[5:])
print(list1[-3:-1])
print(list1[2:5:2])
result = []
for i in 'Vineeth':
    result.append(i)
print('Now the value of result variable is: ',result)
result_1 = list()
result_1 = [i for i in 'inmakes']
print(result_1)
result_2 = [k for k in 'Revathy Nivas']
print(result_2)
new = []
pl = ['C','Python','PHP','Django','Android']
print('Programming Lang.: ',pl)
for i in pl:
    if 'p' in i:
        new.append(i)
print('filtered list:',new)
var1 = ["inmakes" for i in pl]
print(var1)