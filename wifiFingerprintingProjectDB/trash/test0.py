# File: test0.py
# step1
# python test0.py > cmd.dat
import random


file = open("wifiFingerPrinting.txt")
for line in file:
    sStr1 = line.split(' ')
    if sStr1[0] == 'Bedroom':
       sStr1[0] = '1'
    if sStr1[0] == 'Bathroom':
       sStr1[0] = '2'
    if sStr1[0] == 'LivingRoom':
       sStr1[0] = '3'
    if sStr1[0] == 'Kitchen':
       sStr1[0] = '3'
    if sStr1[0] == 'DiningTable':
       sStr1[0] = '3'
    rand = random.randint(1,800)
    rStr = str(rand)+'\t'+sStr1[0]+'\t'
    i = 1
    for ssStr in sStr1[1:]:
        rStr += str(i)+':'+ssStr+'\t'
        i = i+1
    print rStr[:-2]
file.close()

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
