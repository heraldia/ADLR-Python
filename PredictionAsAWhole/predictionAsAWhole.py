soundDbTest = 'soundDbTest.dat'
wifiDbTest = 'wifiDbTest1.dat'
wifiPrediction = 'wifiPrediction.dat'
orientationPrediction = 'orientationPrediction.dat'
soundPrediction = 'soundPrediction.dat'

predictionOutputArff = 'predictOutput.arff'
predictionOutputDat = 'predictOutput.dat'

setInforFile = 'setInfor.dat'

def predictionAsAWholeArff(activitySet,soundSet):
    fSoundDbTest = file(soundDbTest,'r')
    fWifiDbTest = file(wifiDbTest,'r')
    fwifiPrediction = file(wifiPrediction,'r')
    fSound = file(soundPrediction,'r')
    fOrientation = file(orientationPrediction,'r')
    #fWifi = file(wifiPrediction,'r')
    fout = file(predictionOutputArff, 'w')
    fout.write("@RELATION activityRelation\n")
    fout.write("\n")

    activityUString = ''
    countActi = 0
    for activityU in activitySet:
        activityUString += ','+activityU
        #activityUString += ','+str(countActi)
        countActi += 1

    activityUString = activityUString.replace(',','',1)


    fout.write("@ATTRIBUTE orientation numeric\n")
    fout.write("@ATTRIBUTE soundPredictionResult numeric\n")
    fout.write("@ATTRIBUTE wifiPredictionResult numeric\n")
    fout.write("@ATTRIBUTE time numeric\n")
    fout.write("@ATTRIBUTE activity {%s}\n"%activityUString)

    fout.write("\n")
    fout.write("@DATA\n")
    for line in fSoundDbTest.readlines():
        strs = line.split('\t')
        activity =strs[0].strip()
        #print activity
        orientation =strs[1].strip()
        angle =strs[2].strip()
        soundFile =strs[3].strip()
        time = soundFile[9:11]
        #print soundFile
        #time =strs[4].strip()
        if soundFile:
            soundPredictionResult = searchInSoundFile(soundFile, soundPrediction)
        elif not soundFile :
            soundPredictionResult = "NoneFile"
            #time = str(-1)
            time = '?'

        wifiPredictionResult, wifiPredictionResultN = searchInWifiFileReturnRoom(time, wifiPrediction)

        orientationPredictResult = searchInOrientationFile(orientation,orientationPrediction)

        activity = filter(str.isalpha, activity)
        soundPredictionResult = filter(str.isalpha, soundPredictionResult)

        '''
        fout.write(activity + '\t' + \
                orientation + '\t' + \
                #orientationPredictResult + '\t' + \
                soundPredictionResult \
                + '\t' + wifiPredictionResult \
                + '\t' + time \
                + '\n')
                '''
        orientationN = orientationTransform(orientation)

        if wifiPredictionResultN > -1:
            fout.write(
                    str(orientationN) + ',' + \
                    #orientationPredictResult + ',\t' + \
                    soundTransform(soundPredictionResult,soundSet) \
                    + ',' + str(wifiPredictionResultN) \
                    + ',' + time \
                    + ',' + activity \
                    +'\n')

        '''
        fout.write("'"+ activity + "'" + '\t' + \
                "'" + orientation + "'"+ '\t' + \
                #orientationPredictResult + '\t' + \
                 "'" + soundPredictionResult + "'"\
                + '\t' + "'"+ wifiPredictionResult + "'"\
                + '\t'  + "'"+ time + "'"\
                + '\n')
        '''
        """
        + '\t= ' + \
        finalPredictResult
        """
    fout.close()


def predictionAsAWholeDat():
    fSoundDbTest = file(soundDbTest,'r')
    fWifiDbTest = file(wifiDbTest,'r')
    fwifiPrediction = file(wifiPrediction,'r')
    fSound = file(soundPrediction,'r')
    fOrientation = file(orientationPrediction,'r')
    #fWifi = file(wifiPrediction,'r')
    fout = file(predictionOutputDat, 'w')
    activitySet = set()
    soundSet = set()

    for line in fSoundDbTest.readlines():
        strs = line.split('\t')
        activity =strs[0].strip()
        #print activity
        orientation =strs[1].strip()
        angle =strs[2].strip()
        soundFile =strs[3].strip()
        time = soundFile[9:11]
        #print soundFile
        #time =strs[4].strip()
        if soundFile:
            soundPredictionResult = searchInSoundFile(soundFile, soundPrediction)
        elif not soundFile :
            #soundPredictionResult = "NoneFile"
            soundPredictionResult = "?"
            time = '?'
            #time = str(-1)

        wifiPredictionResult, wifiPredictionResultN = searchInWifiFileReturnRoom(time, wifiPrediction)

        orientationPredictResult = searchInOrientationFile(orientation,orientationPrediction)

        finalPredictResult = decide(orientation, soundPrediction, wifiPredictionResult)

        activity = filter(str.isalpha, activity)
        activitySet.add(activity)
        #soundPredictionResult = filter(str.isalpha, soundPredictionResult)
        soundSet.add(soundPredictionResult)

        '''
        fout.write(activity + '\t' + \
                orientation + '\t' + \
                #orientationPredictResult + '\t' + \
                soundPredictionResult \
                + '\t' + wifiPredictionResult \
                + '\t' + time \
                + '\n')
                '''

        fout.write(activity + ',' + \
                orientation + ',' + \
                #orientationPredictResult + ',\t' + \
                soundPredictionResult \
                + ',' + wifiPredictionResult[0] \
                + ',' + time \
                + '\n')

        '''
        fout.write("'"+ activity + "'" + '\t' + \
                "'" + orientation + "'"+ '\t' + \
                #orientationPredictResult + '\t' + \
                 "'" + soundPredictionResult + "'"\
                + '\t' + "'"+ wifiPredictionResult + "'"\
                + '\t'  + "'"+ time + "'"\
                + '\n')
        '''
        """
        + '\t= ' + \
        finalPredictResult
        """
    fout.close()
    return activitySet,soundSet


def decide(orientation, soundPrediction, wifiPredictionResult):
    orientation = orientation.strip()
    soundPrediction = soundPrediction.strip()
    wifiPredictionResult = wifiPredictionResult[0].strip()
    soundSet1 = ['cooking', 'cooking2', 'cooking3' ]
    soundSet2 = ['washing', 'bathroom' ]
    wifiSet = []
    oriSet1 = ['NW','N','NE'] # Breakfast, Lunch, Eating, Dinner, Midnight snack
    oriSet2 = ['SW','S','SE'] # Cooking
    oriSet3 = ['NE','E','SE'] #
    oriSet4 = ['NW','W','SW'] # Washing dishes, Washing in bathroom, Bathroom
    resultSet = []
    actiSet1 =['Breakfast', 'Lunch', 'Eating', 'Dinner', 'Midnight snack']
    actiSet2 =['Cooking']
    actiSet3 =['Washing dishes', 'Washing in bathroom', 'Bathroom']
    loca1 = 'Bathroom'
    loca2 = 'Kitchen'

    if orientation in oriSet1:
        resultSet += actiSet1
    if orientation in oriSet2:
        resultSet += actiSet2
    if orientation in oriSet3:
        pass
    if orientation in oriSet4:
        resultSet += actiSet3

    #print resultSet
    if soundPrediction in soundSet2:
        if loca1 in resultSet:
            result = actiSet3[1]
            print result
            return result

    if soundPrediction == 'cooking3':
        if loca2 :
            result = 'Eating'
            return result

    #return decide
    return 'Y'

def searchInSoundFile(target, soundPrediction):
    #print target
    fSound = file(soundPrediction,'r')
    for line in fSound.readlines():
        strss = line.split('\t')
        #print strs
        #print type(strs)
        #l = -1
        for strs in strss:
            #print strs
            l = strs.find(target)
            #print l
            if l > -1:
                #print target
                #print line
                return strss[2].strip()
            elif l == -1:
                #print target
                continue
            else:
                pass
    return 'None'
    fSound.close()


def searchInWifiFileReturnRoom(time, wifiPrediction):
    l = int(searchInWifiFile(time,wifiPrediction))
    if l == 1 :
        return "Bedroom",1
    elif l == 2:
        return "Bathroom",2
    elif l == 4:
        return "Kitchen",4
    else:
        return "Unknown",-1

def searchInWifiFile(time, wifiPrediction):
    #print time
    fwifiPrediction = file(wifiPrediction,'r')
    for line in fwifiPrediction.readlines():
        strss = line.split('\t')
        for strs in strss:
            #print strs
            l = strs.find(time)
            #print l
            if l > -1:
                #print time
                #print strss[0]
                return strss[0]
            elif l == -1:
                #print time
                continue
            else:
                pass
    fwifiPrediction.close()
    return '-1'

def searchInOrientationFile(orientation, orientationPrediction):
    fSound = file(soundPrediction,'r')
    return "N"
    pass


def test():
    a = '20141006_131524'
    b = ' Breakfast 	N 	12.0 	20141006_131524 	2014-10-06 13:15:29 '
    ba = b.split('\t')
    for l in ba:
        print l.find(a)

def test1():
    target = '2041022_233039'
    a = searchInSoundFile(target,soundPrediction)
    print a

def test2():
    wifiPrediction  = 'wifiPrediction.dat'
    time = '2014-10-25 23:24:15'
    #wifiPredictionResult = searchInWifiFile(time, wifiPrediction)
    #print wifiPredictionResult
    #print searchInWifiFileReturnRoom(time, wifiPrediction)

def orientationTransform(orientation):
    orienSet = ('N','NE','E','SE','S','SW','W','NW')
    sqeN = 0
    for ori in orienSet:
        if orientation == ori:
            return sqeN
        sqeN += 1
    return '?'


def soundTransform(soundPredictionResult,soundSet):
    soundPredictionResultN = 0
    if  soundPredictionResult == "NoneFile":
        return "?"
    for soundU in soundSet:
        #print soundU
        if soundU == soundPredictionResult:
            return str(soundPredictionResultN)
        soundPredictionResultN += 1
    #return str(-1)
    return '?'

def setInfor(activitySet,soundSet):
    fout = file(setInforFile, 'w')
    fout.write('activitySet-------------\n')
    actiN = 0
    for acti in activitySet:
        fout.write(acti+','+str(actiN)+'\n')
        actiN += 1

    fout.write('\nsoundSet-------------\n')
    soundN = 0
    for sound in soundSet:
        fout.write(sound+','+str(soundN)+'\n')
        soundN += 1

    fout.write('\nlocalSet-------------\n')
    locacDic ={ "Bedroom":1,
            "Bathroom":2,
            "Kitchen":4,
            "None / ?":0,
            "Unknown":-1 }
    for loc in locacDic:
        fout.write(loc + ","+str(locacDic[loc])+'\n')

    return 1


if __name__ == '__main__':
     #soundvitySet = set()
     activitySet, soundSet = predictionAsAWholeDat()
     predictionAsAWholeArff(activitySet,soundSet)
     setInfor(activitySet,soundSet)
     #test1()

