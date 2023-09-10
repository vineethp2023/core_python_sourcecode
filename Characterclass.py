import re
pattern ="[A-Z][a-z][0-9]"
if re.search(pattern,'Pe2S'):
    print('Pattern okay')
else:
    print('Pattern not okay')