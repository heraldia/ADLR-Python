filename  = 'lightanglehourxAcceyAccezAccrM.withPrediction.txt'
misClassficationDict = {}

for ele in open(filename):
    printBoolean = True
    eleList = ele.split(',')
    adlList1 = [9,8,13,14,18]
    adlList2 = [9,8]
    adlResult1 = eleList[1].split(':')[1]
    adlResult2 = eleList[2].split(':')[1]
    adlResultId1 = int(eleList[1].split(':')[0])
    adlResultId2 = int(eleList[2].split(':')[0])
    hour = eleList[3]

    if adlResult1 in adlResult2:
        printBoolean = False

    if adlResultId1 in adlList1 and adlResultId2 in adlList1:
        printBoolean = False
        pass
    if adlResultId1==9 and adlResultId2==14:
        printBoolean = False
    if adlResultId1==7 and adlResultId2==8:
        printBoolean = False
    if adlResultId1==10 and adlResultId2==19:
        printBoolean = False
    if adlResultId1==19 and adlResultId2==17: #todo
        printBoolean = False
    if adlResultId1==7 and adlResultId2==18:
        printBoolean = False
    if adlResultId2==7 and adlResultId1==18:
        printBoolean = False
    if adlResultId1==7 and adlResultId2==8:
        printBoolean = False
    if adlResultId1==18 and adlResultId2==8:
        printBoolean = False
    if adlResultId2==18 and adlResultId1==8:
        printBoolean = False
    if adlResultId1==15 and adlResultId2==19:
        printBoolean = False
    if adlResultId1==13 and adlResultId2==9:
        printBoolean = False
    if adlResultId1==11 and adlResultId2==19:
        printBoolean = False

    if adlResultId1== adlResultId2:
        printBoolean = False


    if printBoolean:
        tupleX = (adlResult1,adlResult2, hour)
        if tupleX not in misClassficationDict:
            misClassficationDict[tupleX] = 1
        else :
            misClassficationDict[tupleX] += 1
        print ele.replace('\n','')


'''
def printRuselt(misClassficationDict):
        #print the result
        for key in misClassficationDict.keys():
            print key + ":" + str(misClassficationDict[key])
'''
print '-'*30
dict= sorted(misClassficationDict.iteritems(), key=lambda d:d[1], reverse = True)
for ele in dict :
    print ele

#printRuselt(misClassficationDict)
#print misClassficationDict
print '-'*30
dict= sorted(misClassficationDict.iteritems(), key=lambda d:d[0])
for ele in dict :
    print ele
