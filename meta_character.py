import re
var1 = "Hello, Welcome all"
var2 = 'H.l'
if re.match(var2,var1):
    print('Word found')
else:
    print('Word not found')