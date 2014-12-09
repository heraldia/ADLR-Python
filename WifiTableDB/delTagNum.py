
file = open("test.dat")
for line in file:
    sStr1 = line.split('\t')
    rStr = sStr1[0]
    rStr += '\t'
    for i in range(1,9):
        #colonPosition = sStr1[i].index(':')
        rStr += sStr1[i][2:]
        rStr += '\t'
    print rStr[:-2]
file.close()



