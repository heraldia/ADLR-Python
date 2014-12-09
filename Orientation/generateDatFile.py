import re
import os
from activityCountSet import *

patt = re.compile(r'^[-1]', re.I|re.U|re.X)

def generateActivitySet():
    #filenames = ['Dinner', 'Cooking', 'Washing', 'Bathroom', 'Working',\
    #        'Lunch','Breakfast', 'Eating', 'Midnight', 'Music']
    activity_set = set()
    f1 = file('activityList.txt', 'r')
    for line in f1.readlines():
        sStr = line.split('\t')
        strsub = sStr[0].strip()
        if  strsub != '':
            activity_set.add(strsub)

    f1.close()
    return activity_set

def generateClassiFile(activity_set):
    for filename in activity_set:
        f1 = file('activityList.txt', 'r')
        fresult = file(filename+'.dat', 'w')
        for line in f1.readlines():
            '''
            if not patt.match(line) :
                continue
            else:
            '''
            if filename in line:
                fresult.write(line);
        fresult.close()
        f1.close()


def generateReport():
    import glob
    for filename in glob.glob(r'*.dat'):
        if filename != 'Report_distri.dat':
            objSetActiOriePairNames = writeDistribute(filename)
        infor(objSetActiOriePairNames)
        print "-"*20

def writeDistribute(fileName):
    f1 = file(fileName, 'r')
    #fOut = file("Report.dat",'w')
    orientationSet = set()
    activitySet = set()
    objSetActiOriePairNames  = set()
    for line in f1.readlines():
        sStr = line.split('\t')
        activity = sStr[0].strip()
        orientation = sStr[1].strip()
        activitySet.add(activity)
        orientationSet.add(orientation)
    #print activitySet,orientationSet

    for acti in activitySet:
        for ori in orientationSet:
            actiOriePairNameObj = ActivitiesOrientationPair(acti,ori)
            actiOriePairNameS = ActivityCountSet(actiOriePairNameObj)
            objSetActiOriePairNames.add(actiOriePairNameS)
    f1.close()

    f1 = file(fileName, 'r')
    for line in f1.readlines():
        sStr = line.split('\t')
        activity_m = sStr[0].strip()
        orientation_m = sStr[1].strip()
        for obj in objSetActiOriePairNames :
            if obj.isEqual(activity_m,orientation_m):
                obj.increment()
    f1.close()
    #fOut.close()

#    for obj in objSetActiOriePairNames :
#       obj.infor()

    return objSetActiOriePairNames

def inform(objSetActiOriePairNames):
    for obj in objSetActiOriePairNames :
       obj.infor()

def infor(objSetActiOriePairNames):
    #fid=file('2.txt','a')
    orienSet = ['N','NE','E','SE','S','SW','W','NW']
    c = 0
    for orie in orienSet:
        for obj in objSetActiOriePairNames :
            if orie == obj.orientation :
                print '%s\t'%(str(c)),
                obj.infor()
                c=c+1
                #continue
            #continue


    #fid.flush()
    #fid.close()

if __name__=="__main__":

    os.system('del *.dat')
    activity_set = generateActivitySet()
    #print activity_set
    generateClassiFile(activity_set)

    generateReport()

