print('Enter a limit: ')
k = int(input())
li = list()
print('Enter ', k ,' numbers\n')
for i in range(k):
    k = int(input())
    li.append(k)
print('The list of numbers created\n',li)
print('The sub list created from the above list is\n')
low = 2
high = 5
sl = li[low:high]
print(sl)
print('List comprehension using string formatting\n')
print('{0},{1},{2},{3}'.format(li[2],li[3],li[4],li[5]))
print('The values from the index 2 to 6 are\n')
print(li[2:7])
print('Second last element is ',li[-2])
print('Creating a tuple below')
tuple1 = ()
tuple1 = ('Pen',2,'Car','Pencil','Bike')
print(tuple1)
print('After adding one more element, tuple is \n')
temp = list(tuple1)
temp.insert(len(temp),'Cycle')
tuple1 = tuple(temp)
print(tuple1)
temp = list(tuple1)
temp.append('TV')
print('After appending , the tuple is\n')
tuple1 = tuple(temp)
print(tuple1)




