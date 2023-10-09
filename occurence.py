n = int(input("Enter a number\n"))
list1 = list()
visited = list()
print("\n Enter ",n," elements\n")
for i in range(0,n):
    list1.append(int(input()))
print("entered list is ",list1)
for i in list1:
    count = 0
    for j in range(0,len(list1)):
        if i==list1[j]:
            count = count+1
    if i not in visited:
        print('Occurences of the number ',i,' is: ',count)
    visited.append(i)
    
    
