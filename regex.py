import re
tofinder = 'Vineeth'
content = 'Afueth,Yedhu,Vineeth,Melbin,DK,Ahalya,Cyri,Jobin,Mathew,Nikhil,Sanio,Tanmay'
if re.search(tofinder,content):
    print('Matched')
else:
    print('Not matched')
if re.match(tofinder,content):
    print('Matched...')
else:
    print('Unmatched')
pattern = 'python'
print(re.findall(pattern,'Python is robust,simple and powerful,python and java is object oriented, python is open source'))