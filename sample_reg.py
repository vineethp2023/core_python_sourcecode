import re
tofinder = 'Vineeth'
content = 'Afueth,Yedhu,Vineeth,Melbin,DK,Ahalya,Cyri,Jobin,Mathew,Nikhil,Sanio,Tanmay'
if re.search(tofinder,content):
    print('Matched...')
else:
    print('Unmatched')