import os
import glob

excepta = ['Bathroom1st33','Bathroom1stpee', 'Dinner33','Testing','Walkingoutside', 'WorkingonPCathomemusic','Bus','Runningoutside','Stategym','WalkingAtHome','Bathroomfaucetdrip','boiling']
livingroomAdls = [ 'Breakfast','Chop','Cooking','Dinner', 'LivingRoom', 'Lunch','Midnightsnack', 'Washingdishes' ]
bedroomAdls = ['Dinnerbedroom','Gettingup', 'Nap', 'Sleep', 'WorkingonPCathome']

pathp1 = r' ../../Android/NexusSensors/DbRecords/AS/Phil/'.lstrip()
pathp2 = r' ../../Android/NexusSensors/DbRecords/AS/db19/valuable/'.lstrip()
pathp3 = r' ../../Android/NexusSensors/DbRecords/AS/db19/working/'.lstrip()


def printActionList1(pathplist): # indoor adls

    actionset = set()
    for ele in pathplist:
        for filecsv in glob.glob(ele+'*.csv'):
            for line in open(filecsv):
                if '&' not in line and 'wifiap' not in line:
                    #print line.replace('\n','')

                    boolen_flg = False
                    for elx in excepta:
                        if elx in line.replace(' ',''):
                            boolen_flg = True
                            break
                    if not boolen_flg:
                        line = line.split(',')
                        actionset.add(line[12].replace(' ',''))
                    break
    actionlist = list(actionset)
    actionlist.sort()
    print actionlist
    return actionlist

def printActionList(pathplist):

    actionset = set()
    for ele in pathplist:
        for filecsv in glob.glob(ele+'*.csv'):
            for line in open(filecsv):
                if '&' not in line and 'wifiap' not in line:
                    #print line.replace('\n','')

                    boolen_flg = False
                    for elx in livingroomAdls:
                        if elx in line.replace(' ',''):
                            boolen_flg = True
                            break
                    if boolen_flg:
                        line = line.split(',')
                        actionset.add(line[12].replace(' ',''))
                    break
    actionlist = list(actionset)
    actionlist.sort()
    print actionlist
    return actionlist


def getAngle():
    res = {}
    for fileCsv in glob.glob(pathp1+'*.csv'):

        #resultLine = []
        for line in open(fileCsv):
            #print line.replace('\n','')
            line = line.split(',')
            if not res.has_key(line[12]):
                _templist = []
                res[line[12]] = _templist
            else:
                #res[line[12]].append(line[0])
                res[line[12]].append(line[4])
            break
    print res


def generateArff(pathPList):
    predictionOutputArff = 'predictOutput.arff'
    argList = ['light','angle','hour' , 'location', 'xAcce', 'yAcce', 'zAccr']
    predictionOutputArff = open(predictionOutputArff,'w')
    relation = "@relation '"+"".join(argList) +"'\n\n"
    predictionOutputArff.writelines(relation)

    for i,e in enumerate(argList):
        _ts = '@attribute \'%s\' real\n'%e
        predictionOutputArff.writelines(_ts)

    _s = str(printActionList(pathPList)).replace('[','').replace(']','').replace(' ','')
    s = '@attribute \'class\' { %s}\n'%_s
    predictionOutputArff.writelines(s)
    predictionOutputArff.writelines('\n@data\n')


    for ele in pathPList:
        for fileCsv in glob.glob(ele+'*.csv'):
            filename = os.path.splitext(os.path.basename(fileCsv))[0].replace('Living_','')
            for line in open(fileCsv):
                boolen_flg = False
                if '&' not in line and '@' not in line:
                    for elx in excepta:
                        if elx in line.replace(' ',''):
                            boolen_flg = True
                            break
                    if not boolen_flg:
                        line = line.split(',')

                        processedLine0 = line[0].split('.')[0]+'.'+line[0].split('.')[1][:2]
                        hour = os.path.basename(fileCsv).split('_')[2][:2]

                        actionLabel =  line[12].replace(' ','')
                        #if actionLabel == 'Eating': actionLabel = 'Midnightsnack'
                        #if actionLabel == 'Cookinglast4speech': actionLabel = 'Cooking'

                        location = generateLocation(actionLabel)
                        predictionOutputArff.write(processedLine0+','+line[4]+','+hour+',' +location + ',' +\
                                line[1] + ',' + \
                                line[2] + ',' +\
                                line[3] + \
                                ','+actionLabel+' % '+filename+'\n')
                        #print filename
                        #predictionOutputArff.write('\n')
                    break

    predictionOutputArff.close()

import random
def generateLocation(actionLabel):

    if actionLabel in ['Amespubliclibrary']: location = 0
    elif actionLabel in [ 'Bathroombowel', 'Bathroomfaucet', 'Bathroomflushing', 'Bathroompee'] : location = random.randint(1,4)
    elif actionLabel in [ 'Breakfast', 'Dinner', 'Midnightsnack', 'LivingRoom', 'Lunch'] : location = random.randint(1,4)
    elif actionLabel in [ 'Chop', 'Cooking', 'Washingdishes'] : location =   random.randint(1,4)
    elif actionLabel in [ 'Nap', 'Sleep', 'Dinnerbedroom', 'Gettingup', 'WorkingonPCathome' ] : location =  random.randint(1,4)
    elif actionLabel in [ 'PCoffice'] : location = 5
    elif actionLabel in [ 'gilman1353' ] : location = 6
    elif actionLabel in [ 'rs' ] : location = 7
    else: location = 9

    return str(location)
    pass


def searchFiles(actionName):
#    actionName = 'diahes'
    for fileCsv in glob.glob(pathp1+'*.csv'):
        for line in open(fileCsv):
            line = line.split(',')

            #print line[12]
            if actionName in line :
                print os.path.basename(fileCsv)
            break



if __name__ == '__main__':
    pathPList = [pathp1,pathp2,pathp3]
    generateArff(pathPList)
    #searchFiles('Go to sleep')
    #printActionList(pathPList)

