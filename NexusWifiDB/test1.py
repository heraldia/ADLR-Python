# File: test1.py
# step1
# python test1.py > cmd.dat

file = open("wifiFingerPrinting1.txt")
for line in file:
    sStr1 = line.split(' ')
    rStr = sStr1[0]
    rStr += '\t'
    #print rStr
    #rStr += '\t'
    #print sStr1[1]
     #for ssStr1 in sStr1[1]:
      # print ssStr1
    #sStr1[1].replace("\n","")
    #sStr2 = sStr1[1].split('\t')
    i = 1
    for i in range(1,9):
        rStr += str(i)
        rStr += ':'
        rStr += sStr1[i]
        rStr += '\t'
        i = i+1
    print rStr[:-2]
file.close()



