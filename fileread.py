file1 = open('demo.txt','r')
if file1 != '\0':
    print(file1.read())
    file1.close()
