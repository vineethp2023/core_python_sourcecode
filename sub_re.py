import re
str = "Hello, Welcome to the world of programming"
new_str = re.sub('programming','python',str)
print('Old string: ',str)
print('\n new string: ',new_str)