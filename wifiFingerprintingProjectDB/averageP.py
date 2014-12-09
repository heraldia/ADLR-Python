import glob
import re
import os

_DEBUG = False

def averageP():

    with open('wifiFingerPrinting.txt','r') as f:
        with open('averageWifiFingerPrinting.txt','w') as f1:
            #f = file('wifiFingerPrinting.txt','r')
            for line in f.readlines():
                #print line
                line = re.sub('\n','',line)
                stra = line.split(' ')
                numL = [int(i) for i in stra[1:9]]
                #print numL
                #print sum(numL)
                #Average(numL)
                f1.write(stra[0] + '\t'+ str(Average(numL))+'\n')

def Average(list):
    return round(float(sum(list))/float(len(list)), 3)

if __name__=="__main__":
    averageP()
    if _DEBUG == True:
        pass
