import os
import glob

def getAllADLLables(user = 'Faythe'): #{{{2
    dirx = (' ../../Android/NexusSensors/DbRecords/AS/%s/*.csv'%user).lstrip()
    ADLset = set()
    toDetail = ['fb','lib','chat','vocabulary','class']
    toChange = ['library']
    for csvFile in glob.glob(dirx):
        for line in open(csvFile):
            adlLabel =  line.split(',')[12]
            ADLset.add(adlLabel.replace(' ',''))
            for ele in toDetail:
                if ele in adlLabel:
                    #print os.path.basename(csvFile)
                    break
            break
    return list(ADLset)

def getAllMac(user = 'Faythe'): # no use
    dirx = (' ../../Android/NexusSensors/DbRecords/AS/%s/*.csv'%user).lstrip()
    macSet = set()
    for csvFile in glob.glob(dirx):
        count = 0
        for line in open(csvFile):
            if count != 0 and ":" in line:
                eleMac =  line.split(',')[0]
                macSet.add(eleMac)
            count += 1

    print list(macSet)

def getSensorData(user = 'Faythe'): #{{{2
    dirx = (' ../../Android/NexusSensors/DbRecords/AS/%s/*.csv'%user).lstrip()
    totalOutput = ''
    for csvFile in glob.glob(dirx):
        count = 0
        cc = 0
        output = ''
        mac = ''
        gsm = ''
        for line in open(csvFile):
            if count == 0 :
                ele =  line.split(',')
                output = ele[4]+',' \
                        +ele[9]+',' \
                        +ele[10]+',' \
                        +ele[11]+','
                adlLabel = ele[12]
                if '_' in ele[13]:
                    output += ele[13].split('_')[1][0:2]+','
                elif '_' in ele[14]:
                    output += ele[14].split('_')[1][0:2]+','

            elif count != 0 and ":" in line and cc < 5 and 'coord' not in line:
                #eleMac =  line.split('&')
                eleMac =  line.split(',')
                mac = mac2parts(eleMac[0])+','+eleMac[2] + ','
                output += mac
                cc += 1

            elif count != 0 and not ':' in line:
                gsm = line.replace('\n',',')
                output += gsm


            count += 1
        output = output + adlLabel.replace(' ','') + ' % ' + os.path.splitext(os.path.basename(csvFile))[0]
        output += '\n'
        totalOutput += output

    return totalOutput,len(totalOutput.split('\n')[0].split(','))

    '''
    elif not mac:
        output += '-1,'*4*2
    '''
    '''
    elif not gsm:
        output += '-1,'*3
    '''

def getSensorDataIndoorLabels(indoorAdlList, user = 'Faythe'): #{{{2
    #indoorAdlList = ['WorkingonPC','Bathroom','Nap','dryclothes','bake','Eating','Gettingup','Boiling','WalkingAtHome','laundry','Midnightsnack','cook','WorkingonPCathome','Bathroomflushing','study','Sleep']
    dirx = (' ../../Android/NexusSensors/DbRecords/AS/%s/*.csv'%user).lstrip()
    totalOutput = ''
    for csvFile in glob.glob(dirx):
        count = 0
        cc = 0
        output = ''
        mac = ''
        gsm = ''
        for line in open(csvFile):
            if count == 0 :
                ele =  line.split(',')
                adlLabel = ele[12]
                output = ele[4]+',' \
                        +ele[9]+',' \
                        +ele[10]+',' \
                        +ele[11]+','
                if '_' in ele[13]:
                    output += ele[13].split('_')[1][0:2]+','
                elif '_' in ele[14]:
                    output += ele[14].split('_')[1][0:2]+','

            elif count != 0 and ":" in line and cc < 5:
                eleMac =  line.split(',')
                mac = mac2parts(eleMac[0])+','+eleMac[2] + ','
                output += mac
                cc += 1

            elif count != 0 and not ':' in line:
                gsm = line.replace('\n',',')
                output += gsm


            count += 1
        output = output + adlLabel.replace(' ','') + ' % ' + os.path.splitext(os.path.basename(csvFile))[0]
        output += '\n'
        if adlLabel.replace(' ','') in indoorAdlList:
            totalOutput += output

    return totalOutput,len(totalOutput.split('\n')[0].split(','))

def generateArffAllLabel(user = 'Faythe'): #{{{1
    predictionOutputArff = 'predictOutput.arff'
    #argList = ['light','angle','hour']
    predictionOutputArff = open(predictionOutputArff,'w')
    relation = "@relation '"+ user +"'\n\n"
    predictionOutputArff.writelines(relation)

    output , columnNum = getSensorData(user)   # see [line70]
    for i in xrange(1,columnNum):
        s = '@attribute \'term%d\' real\n'%i
        predictionOutputArff.writelines(s)

    _s = getAllADLLables(user)
    s = '@attribute \'class\' { %s}\n'%_s
    predictionOutputArff.writelines(s.replace(' ' ,'').replace('[','').replace(']',''))
    predictionOutputArff.writelines('\n@data\n')
    predictionOutputArff.writelines(output)

    predictionOutputArff.close()

def generateArffIndoorLabel(user = 'Faythe'): #{{{1
    predictionOutputArff = 'predictOutput.arff'
    predictionOutputArff = open(predictionOutputArff,'w')
    relation = "@relation '"+ user +"'\n\n"
    predictionOutputArff.writelines(relation)

    indoorAdlList = ['WorkingonPC','Bathroom','Nap','dryclothes','bake','Eating','Gettingup','Boiling','WalkingAtHome','laundry','Midnightsnack','cook','WorkingonPCathome','Bathroomflushing','study','Sleep']
    outdoorAdlList = ['Gilman','hyvee', 'VisitFriend','TJtea','durham','ParksLibrary','Bar','Coover','Bus','Sweeney','Pearson','blackengineering','Science','mogoliangrill','lib','NewChina','Howe','pearson','Mackay','mu','Hub','Lied','ScienceII','MusicHall','Sleep','Atanasoff','LebaronHall','WaitingBus']

    output , columnNum = getSensorDataIndoorLabels(outdoorAdlList, user)   # see [line70]
    for i in xrange(1,columnNum):
        s = '@attribute \'term%d\' real\n'%i
        predictionOutputArff.writelines(s)

    _s = outdoorAdlList
    s = '@attribute \'class\' { %s}\n'%_s
    predictionOutputArff.writelines(s.replace(' ' ,'').replace('[','').replace(']',''))
    predictionOutputArff.writelines('\n@data\n')
    predictionOutputArff.writelines(output)


    predictionOutputArff.close()

def mac2parts( s = '00:00:00:00:00:00'):
    s = s.split(':')
    f1 = s[0]+s[1]+s[2]
    f2 = s[3]+s[4]+s[5]
    return hex2dec(f1)+','+ hex2dec(f2)
    #print hex2dec('AA')

def hex2dec(string_num):
    return str(int(string_num.upper(), 16))

def summaryArff():
    arffFile = 'predictOutput.arff'
    Flag = False
    numSet = set()
    for line in open(arffFile):
        if '@data' in line:
            Flag = True
            continue
        if Flag:
            numSet.add(len(line.split(',')))
    print numSet
    return numSet

def getPartialADLLables(columnSize):
    arffFile = 'predictOutput.arff'
    adlSet = set()
    Flag = False
    for line in open(arffFile):
        if '@data' in line:
            Flag = True

        line = line.split('%')[0]
        if Flag and len(line.split(','))==columnSize:
            adlSet.add(line.split(',')[-1].rstrip())
    return list(adlSet)


def splitFiles():
    #numberFile = size(summaryArff())
    arffFile = 'predictOutput.arff'
    columnSizes = list(summaryArff())
    for columnSize in columnSizes:
        adlSet = set()
        outputArffFile = open( 'predictOutput24.arff'.replace('24',str(columnSize)),'w')

        #for ele in numberFile:
        Flag = False
        lineCount = 0
        for line in open(arffFile):
            if 'relation' in line:
                outputArffFile.writelines(line.replace('Sue','Sue%d'%columnSize))
                continue
            if not Flag and not 'class' in line and lineCount < columnSize  :
                outputArffFile.writelines(line)
            if Flag:
                if len(line.split(','))==columnSize:
                    linex = line.split('%')[0]
                    adlSet.add(linex.split(',')[-1].rstrip())

            if '@data' in line:
                Flag = True
                _s = getPartialADLLables(columnSize)
                s = '@attribute \'class\' { %s}\n'%_s
                outputArffFile.writelines(s.replace(' ' ,'').replace('[','').replace(']',''))
                outputArffFile.writelines('\n@data\n')

            '''
            if '@data' in line:
                Flag = True
                outputArffFile.writelines(line)
            elif '\n' == line:
                outputArffFile.writelines(line)
            '''

            if Flag:
                if len(line.split(','))==columnSize:
                    outputArffFile.writelines(line)
                    #outputArffFile.writelines('\n')
                    #adlSet.add(line.split(',')[-1].rstrip())
            lineCount += 1
        outputArffFile.close()
        print columnSize, list(adlSet)
    return 1


def matrix2csv(user,number = 24):
    adlList = []
    matrix = 'result/%s/%s.matrix'%(user,number)
    outpFileName = os.path.basename(matrix).replace('.matrix','confusionMatrix.csv')
    outpFile = open(outpFileName,'w')
    for line in open(matrix):
        line = line.replace('  ', ' ')
        #line = line.replace(' |', '  |')
        adlList.append(line.split('|')[-1].strip())
        line = line.replace(' ',',')
        outpFile.writelines(line)
        #print line
    outpFile.close()
    for i, ele in enumerate(adlList):
        print i+1, ele

    errorFileName = outpFileName.replace('confusion','error')

    #=======step2
    errorpFile = open(errorFileName,'w')
    #matrx = []
    with open(outpFileName) as f:
        line = f.readlines()
    lineId = 0
    for ele in line:
        if ele != '\n':
            elex = ele.split(',')
            elex[lineId] = '0'
            elexs = ','.join(elex)
            errorpFile.write( elexs.strip()+'\n')
            lineId += 1
    errorpFile.close()

    #=======step3



def test(mode = 0 , user='Sue'):
    if mode == 0:
        generateArffAllLabel(user)
        splitFiles()
    elif mode == 1:
        generateArffIndoorLabel(user)
        splitFiles()
    elif mode == 2:
        matrix2csv(user)



if __name__ == '__main__':
    #getAllADLLables()
    #getAllMac()
    #getSensorData()

    test(0, 'valuable')



