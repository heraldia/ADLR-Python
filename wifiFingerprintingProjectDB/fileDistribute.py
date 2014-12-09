'''
Created on Sep 26, 2014

@author: Phil
'''
'step 3'

fresulttrain = file('train.dat', 'w')
fresulttest = file('test.dat', 'w')

startPoint = 1
totalPoints = file('cmd1.dat').read().count('\n')
cuttingRate = 0.7
cutPoint = startPoint + cuttingRate*totalPoints - 1
endPoint = startPoint + totalPoints
import glob
for filename in glob.glob(r'.\*1.dat'):
#     print filename
    f1 = file(filename , 'r')

    i = startPoint
    for line in f1.readlines():
        if i >= startPoint  and i<=cutPoint:
            fresulttrain.write(line)
        elif i >cutPoint   and i<=endPoint:
            fresulttest.write(line)
        elif i > endPoint  :
            break
        i+=1
    f1.close()

fresulttrain.close()
fresulttest.close()


# f2.close()
