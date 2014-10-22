# File: test0.py
# step1
# python test0.py > cmd.dat


file = open("wifiFingerPrinting.txt")
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

file.close()


"""
 'Bedroom': '1'
 'Bathroom': '2'
 'LivingRoom': '3'
 'Kitchen': '4'
"""
##    nPos = line.index(nChar)
##    print nPos
##    print line
#    sStr1 = line.split(' ')
#    rStr = sStr1[0]
#    #rStr += '\t'
#    #print sStr1[1]
#     #for ssStr1 in sStr1[1]:
#      # print ssStr1
#    sStr1[1].replace("\n","")
#    sStr2 = sStr1[1].split('\t')
#    i = 1
#    for ssStr2 in sStr2:
#    #for i in range(0,8):
#        rStr += '\t'
#        rStr += str(i)
#        rStr += ':'
#        rStr += ssStr2
#        i = i+1
#    rStr.replace('\t10:\n','')
#    print rStr[:-4]
#    # print sStr2
#
    #print '\t'.join(sStr1)
