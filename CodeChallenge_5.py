file = open('Fileprogram.txt' , 'w')
#writing a file
print('Enter a sentence \n')
sentence = input()
file.write(sentence)
print('Content inputed successfully')
file.close()
# reading file
file = open('Fileprogram.txt','r')
print('The text contains within the file is \n')
print(file.read())
file.close()
# appending content
file = open('Fileprogram.txt','a')
print('Enter a sentence for appending:\n')
sentence = input()
file.write(sentence)
file.close()
file = open('Fileprogram.txt','r')
print('Now full content of the file is\n')
print(file.read())
file.close()
