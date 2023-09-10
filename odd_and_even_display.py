
numlist = [i for i in range(2,223)]
print('Numbers from 2 to 222 are listed below\n')
for j in numlist:
    print(j,end=' ')
print('Even numbers from 2 to 222:\n')
for i in numlist:
    if i % 2 == 0:
        print(i,end='\t')
    else:
        continue
print('Odd numbers from 2 to 222:\n')
for i in numlist:
    if i % 2 != 0:
        print(i,end='\t')
    else:
        continue
