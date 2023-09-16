dict1 = {'pen':5,'pencil':10, 'scale': '20rs', 10: 'rubber'}
print(dict1)
dict2 = {"chair":2000,"table":10000,"almira": 15000,"fridge": 3300}
print(dict2)
print(dict1.keys())
print(dict2['table'])
pl ={
    1: 'C',
    2: 'C++',
    3: 'Java',
    4: 'PHP',
    5: 'Visual Basic',
    6: 'Pascal'
}
print('Programming language dictionary\n')
print(pl)
print('Keys of programming lang.\n')
print(pl.keys())
print('Values of prog. lang.\n')
print(pl.values())
print('Type a new programming language:\n')
pl['7'] = input()
print(pl)
print('Length of the dictionary:\n')
print(len(pl))
pl.update({8:'C#'})
print('updated list: ',pl)
print('removing latest item')
pl.pop(8)
print(pl)
dict1.update({'chair':20})
print(dict1)
dict1.update({'Showcase': 8900})
print(dict1)
dict1.popitem()
print(dict1)
for i in dict2.items():
    print(i)
print('\n')
for i in dict1.keys():
    print(i)
print('\n')
for i in dict2.values():
    print(i)