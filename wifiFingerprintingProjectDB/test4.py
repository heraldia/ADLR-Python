
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
    rStr = sStr1[0]+'\t'
    i = 1
    for ssStr in sStr1[1:]:
        rStr += str(i)+':'+ssStr+'\t'
        i = i+1
    print rStr[:-2]
file.close()
