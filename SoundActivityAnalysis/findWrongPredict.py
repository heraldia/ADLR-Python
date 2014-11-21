import re
import os
from activityPredictionSet import ActivityPredictionSet
from activityPredictionSet import ActivitiesSet


patt = re.compile(r'^[2]', re.I|re.U|re.X)

def generateActivitySet():
    #filenames = ['Dinner', 'Cooking', 'Washing', 'Bathroom', 'Working',\
    #        'Lunch','Breakfast', 'Eating', 'Midnight', 'Music']
    #for filename in filenames:
    activity_set = set()
    f1 = file('activityPrediction.txt', 'r')
    #lineCounter = 0
    for line in f1.readlines():
        #lineCounter +=1
        #if lineCounter < 12:
        if not patt.match(line):
            continue
        else:
            sStr = line.split('\t')
            strsub = sStr[1].strip()
            if  strsub != '':
                activity_set.add(strsub)

    f1.close()
    #activity_set.remove('Working on PC at home')
    return activity_set

def generateClassiFile(activity_set):
    for filename in activity_set:
        f1 = file('activityPrediction.txt', 'r')
        fresult = file(filename+'.dat', 'w')
        for line in f1.readlines():
            if not patt.match(line) :
                continue
            else:
                if filename in line:
                    fresult.write(line);
        fresult.close()
        f1.close()

def generateDiffFile(activity_set, activitiesSet):
    #m_activitiesSet = ActivitiesSet()
    #m_activitiesSet = activitiesSet
    #print activitiesSet
    #print m_activitiesSet
    #print activity_set

    #patt = re.compile(r'^[0-9]', re.I|re.U|re.X)

    for m_activityTuple in activitiesSet.activitiesSet:
        filename = m_activityTuple.actualActivity
        fresult = file(filename+'_diff.dat', 'w')
        fresulNone = file(filename+'_None.dat', 'w')
        f1 = file(filename+'.dat', 'r')
        for line in f1.readlines():
            sStr = line.split('\t')
            targetStr = sStr[2].strip()
            targetStr = filter(str.isalpha, targetStr)
            if not targetStr in m_activityTuple.predictionSet \
                    and targetStr != 'None':
               fresult.write(line)
            if targetStr == 'None':
                fresulNone.write(line)

        fresult.close()
        fresulNone.close()
        f1.close()

    return 0

def createActivityPredictionSet () :
    dinnerSet = set()
    dinnerSet.add('cooking')
    dinnerSet.add('musicandeating')
    dinnerSet.add('eating')
    dinnerPredict = ActivityPredictionSet('Dinner',dinnerSet)

    cookingSet = set()
    cookingSet.add('cooking')
    cookingSet.add('eating')
    cookingSet.add('musicandeating')
    cookingPredict = ActivityPredictionSet('Cooking',cookingSet)

    lunchSet = set()
    lunchSet.add('cooking')
    lunchSet.add('eating')
    lunchSet.add('musicandeating')
    lunchPredict = ActivityPredictionSet('Lunch',lunchSet)

    '''
    eatingSet = set()
    eatingSet.add('cooking')
    eatingSet.add('eating')
    eatingSet.add('musicandeating')
    eatingPredict = ActivityPredictionSet('Eating',eatingSet)
    '''

    breakfastSet = set()
    breakfastSet.add('cooking')
    breakfastSet.add('eating')
    breakfastSet.add('musicandeating')
    breakfastPredict = ActivityPredictionSet('Breakfast',breakfastSet)

    midNightSnackSet = set()
    midNightSnackSet.add('cooking')
    midNightSnackSet.add('eating')
    midNightSnackSet.add('musicandeating')
    midNightSnackPredict = ActivityPredictionSet('MidNight snack',midNightSnackSet)

    bathroomSet = set()
    bathroomSet.add('washing')
    bathroomSet.add('bathroom')
    bathroomPredict = ActivityPredictionSet('Bathroom',bathroomSet)

    washingSet = set()
    washingSet.add('washing')
    washingSet.add('bathroom')
    washingSet.add('cooking')
    washingSet.add('musicandeating')
    washingDishesPredict = ActivityPredictionSet('Washing dishes',washingSet)
    washingInBathroomPredict = ActivityPredictionSet('Washing in bathroom',washingSet)

    '''
    workingOnPcSet = set()
    workingOnPcSet.add('workingonPCathome')
    workingOnPcSet.add('keyboard')
    workingOnPcPredict = ActivityPredictionSet('Working on PC at home',workingOnPcSet)
    '''

    musicOnPcSet = set()
    musicOnPcSet.add('musicandeating')
    musicOnPcPredict = ActivityPredictionSet('Music',musicOnPcSet)

    ###########
    m_activitiesSet = ActivitiesSet()
    m_activitiesSet.addTuple(dinnerPredict)
    m_activitiesSet.addTuple(cookingPredict)
    m_activitiesSet.addTuple(lunchPredict)
    #m_activitiesSet.addTuple(eatingPredict)
    m_activitiesSet.addTuple(breakfastPredict)
    m_activitiesSet.addTuple(midNightSnackPredict)
    m_activitiesSet.addTuple(bathroomPredict)
    m_activitiesSet.addTuple(washingDishesPredict)
    m_activitiesSet.addTuple(washingInBathroomPredict)
    #m_activitiesSet.addTuple(workingOnPcPredict)
    m_activitiesSet.addTuple(musicOnPcPredict)

    #m_activitiesSet.infor()

    return m_activitiesSet


def generateReport(activity_set):
    f1 = file('Report_count.dat', 'w')
    import glob
    for filename in glob.glob(r'*.dat'):
        if filename != 'Report_count.dat':
            num_lines = sum(1 for line in open(filename))
            f1.write("%s\t%s\n"%(filename,num_lines))
    f1.close()

def predictErrorRate():
    # generateReport(activity_set)
    totalSmpCounter = 0
    totalErrorCounter = 0
    totalNoneCounter = 0
    filename = 'Report_count.dat'
    f1 = file(filename, 'r')
    fo = file('Report_rate.dat','w')
    activityDict = {}
    for line in f1.readlines():
        #print line
        sStr = line.split('\t')
        activityName = sStr[0][:-4].lstrip()
        #print activityName
        activityNameFilter = activityName.replace(' ','')
        number = int(sStr[1].lstrip())
        #print number
        if activityNameFilter.isalpha():
            subSmpCounter = 0
            subErrorCounter = 0
            subNoneCounter = 0
            totalSmpCounter += number
            subSmpCounter = number
            activityDict[activityName] = 0
            continue
        elif 'diff' in activityName:
            totalErrorCounter += number
            subErrorCounter = number
        elif 'None' in activityName:
            totalNoneCounter += number
            subNoneCounter = number
            print number
        else:
            pass

        if subSmpCounter > 0 :
            subErrorRate = subErrorCounter / float(subSmpCounter) * 100
            activityDict[activityName] = subErrorRate
            subNoneRate = subNoneCounter / float(subSmpCounter) * 100
        else:
            activityDict[activityName] = 0

        fo.write('%s ---------\n'%activityName)
        fo.write("Sample number is %d\n"%subSmpCounter)
        if 'diff' in activityName:
            fo.write("Error number is %d\n"%subErrorCounter)
            fo.write("Error rate is %f %%\n"%subErrorRate)
        elif 'None' in activityName:
            fo.write("None number is %d\n"%subNoneCounter)
            fo.write("None rate is %f %%\n"%subNoneRate)
        else:
            pass

        #fo.write("None number is %d\n"%subNoneCounter)
        #fo.write("None rate is %f %%\n"%subNoneRate)

    if totalSmpCounter >0 :
        totalErrorRate = totalErrorCounter / float(totalSmpCounter) * 100
        totalNoneRate = totalNoneCounter / float(totalSmpCounter) * 100
        #print totalErrorCounter
        #print totalSmpCounter
        #print totalErrorRate
    else:
        totalErrorRate = 0

    fo.write('\n'+'-'*30+'\n')
    fo.write("Total sample number is %d\n"%totalSmpCounter)
    fo.write("Total error number is %d\n"%totalErrorCounter)
    fo.write("Total error rate is %f %%\n"%totalErrorRate)
    fo.write("Total None number is %d\n"%totalNoneCounter)
    fo.write("Total None rate is %f %%\n"%totalNoneRate)
    fo.close()
    f1.close()



if __name__=="__main__":
    #os.system('del *_diff.dat')
    #os.system('del Walking*')

    os.system('del *.dat')
    activity_set = generateActivitySet()
    activitiesSet = createActivityPredictionSet()
    #activitiesSet.infor()
    generateClassiFile(activity_set)
    generateDiffFile(activity_set, activitiesSet)
    generateReport(activity_set)

    predictErrorRate()


