file = open('demo.txt','w')
if file != '\0':
    print('File created successfully')
else:
    print('File creation failed')
file.close()
