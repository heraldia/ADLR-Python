import glob
from collections import Counter
import os

def countP():
    files = './experiment/2/soundAnalysis/*.dat'
    for filename in glob.glob(files):
        listy = __getListx(filename)
        c = Counter(listy)
        print c

def __getListx(filename):
    filename_x = filename.split('\\')[-1][0:-4]
    print filename_x
    fp = open(filename,'r')
    listx = []
    for line in fp.readlines():
        if ';' in line:
            listx.append( line.strip('\n').split(';')[1])
    fp.close()
    #print listx
    return listx



if __name__ == '__main__':
    countP()
