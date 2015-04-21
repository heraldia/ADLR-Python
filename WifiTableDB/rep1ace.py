# File: test0.py
# step1
# python test0.py > cmd.dat


import re

f1=open('result3.txt','r').read()
f1 = re.sub('Working on PC at home','1',f1)
f1 = re.sub('GettingUp','1',f1)
f1 = re.sub('Getting up','1',f1)
f1 = re.sub('Sleep','1',f1)
f1 = re.sub('Nap','1',f1)
f1 = re.sub('Go to sleep','1',f1)

f1 = re.sub('Bathroom','2',f1)
f1 = re.sub('Shower','2',f1)
f1 = re.sub('Washing in the bathroom','2',f1)
f1 = re.sub('Washing in bathroom','2',f1)

f1 = re.sub('Walking indoor','3',f1)

f1 = re.sub('Breakfast','4',f1)
f1 = re.sub('Lunch','4',f1)
f1 = re.sub('Dinner','4',f1)
f1 = re.sub('Chopping','4',f1)
f1 = re.sub('Cooking','4',f1)
f1 = re.sub('Eating','4',f1)
f1 = re.sub('Midnight snack','4',f1)
f1 = re.sub('Washing dishes','4',f1)

f1 = re.sub('Exercise','5',f1)
f_w=open('wifiFingerPrinting1.txt','wb')
f_w.write(f1)
f_w.close()

"""
 'Bedroom': '1'
 'Bathroom': '2'
 'LivingRoom': '3'
 'Kitchen': '4'
"""
"""
file = open("wifiFingerPrinting.txt")
file.close()
for line in file:
    sStr1 = line.split('-')
#    print sStr1[0]

    if sStr1[0] == 'Working on PC at home' or sStr1[0] == 'GettingUp' \
        or sStr1[0] == 'Sleep':
       sStr1[0] = '1'
    if sStr1[0] == 'Bathroom':
       sStr1[0] = '2'
    if sStr1[0] == 'Walking indoor' or sStr1[0] == 'Lunch' or \
       sStr1[0] == 'Breakfast' or sStr1[0] == 'Dinner':
       sStr1[0] = '3'
    if sStr1[0] == 'Cooking' or sStr1[0] == 'Washing':
       sStr1[0] = '4'
    print sStr1
"""
