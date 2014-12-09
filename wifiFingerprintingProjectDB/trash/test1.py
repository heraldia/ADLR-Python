# File: test1.py
# step1
# python test1.py > cmd.dat

file = open("wifiFingerPrinting.txt")
#nChar = '-'
for line in file:
#    nPos = line.index(nChar)
#    print nPos
#    print line
    sStr1 = line.split(' ')
    rStr = sStr1[0]
    #rStr += '\t'
    #print sStr1[1]
     #for ssStr1 in sStr1[1]:
      # print ssStr1
    sStr1[1].replace("\n","")
    sStr2 = sStr1[1].split('\t')
    i = 1
    for ssStr2 in sStr2:
    #for i in range(0,8):
        rStr += '\t'
        rStr += str(i)
        rStr += ':'
        rStr += ssStr2
        i = i+1
    rStr.replace('\t10:\n','')
    print rStr[:-4]
    # print sStr2

file.close()



