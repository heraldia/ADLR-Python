# File: test0.py
# step1
# python test0.py > cmd.dat

with open("wifiFingerPrinting.txt", "r+") as f:
    d = f.read()
    d.replace("Working on PC at home", "1")
    f.write(d)

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
