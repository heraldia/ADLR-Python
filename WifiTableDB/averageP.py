import glob
import re
import os

#_DEBUG = True
_DEBUG = False

def averageP():
    countLine = 0
    with open('result3.txt','r') as f:
        with open('averageWifiFingerPrinting.txt','w') as f1:
            #f = file('wifiFingerPrinting.txt','r')
            for line in f.readlines():
                countLine += 1
                #print line
                line = re.sub('\n','',line)
                #stra = line.split(' ')
                a1 = line.find('0',1)
                a2 = line.find('-',1)
                if a1 == -1 or a2 ==-1:
                    a = max(a1,a2)
                if a1 > -1 and a2 > -1:
                    a = min(a1,a2)
                if _DEBUG == True:
                    print countLine,a1, a2, a
                #if not a == -1:
                activityName = line[:a-1]
                '''
                if not a == -1:
                    print a
                '''
                stra = line[a:]
                #print stra
                sStra = stra.split(' ')
                numL = [int(i) for i in sStra]
                #print type(stra[0])
                #print len(stra)
                '''
                for i in stra:
                    print i
                    print type(i)
                '''
                #print sStra[0]
                #numL = [int(i) for i in stra]
                #print numL
                #print sum(numL)
                #print Average(numL)
                f1.write(activityName + '\t'+ str(Average(numL))+'\n')

def Average(list):
    return round(float(sum(list))/float(len(list)), 3)

def sortP(appendedFile, outputFile):
    with open(outputFile,'w') as f1:
        l=file(appendedFile).readlines()
        l.sort(key=lambda x:x.lower())
        for i in l:
            #print i
            f1.write(i)
    return l

if __name__=="__main__":
    averageP()
    if _DEBUG == True:
        pass
    l = sortP('averageWifiFingerPrinting.txt','averageWifiFingerPrinting1.txt')
    l1 = sortP('result3.txt','result3P.txt')
    os.system('del averageWifiFingerPrinting.txt')

