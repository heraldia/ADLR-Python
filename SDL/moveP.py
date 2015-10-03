import os
import shutil

#mp3OriginFolder = 'd:\class\Semester5\\research\ADLRecorder\code\Android\DbRecords\soundrecord\mp3\Living_'
mp3OriginFolder = 'd:\class\Semester5\\research\ADLRecorder\code\Android\NexusSensors\DbRecords\soundrecord\mp3\Living_'
amrAllOriginFolder = 'd:\class\Semester5\\research\ADLRecorder\code\Android\DbRecords\soundrecord\\amrAll\Living_'
mp3OriginFolder1 = 'd:\class\Semester5\\research\ADLRecorder\code\python\Sdl\\files'


def __moveP(actionName): # done
    m_filename = actionName +".txt"
    fp = open(m_filename,'r')
    bufferl = fp.readlines()
    folderName = actionName.replace(' ','')
    os.system('mkdir %s'%folderName)
    for line in bufferl:
        data_s = line.split(';')
        #print data_s[0]
        command = 'copy %s %s\\'%(amrAllOriginFolder+data_s[0]+'.amr', folderName)
        print command
        #shutil.copy(command)
        os.system(command)
    fp.close()

def movePW(actionList):
    for actionName in actionList:
        __moveP(actionName)

#statistic
def numberFilesInFolder(actionList):
    tot = 0
    for path in actionList:
        path = path.replace(' ','')
        print path, ': ',
        x = len(sum([i[2] for i in os.walk(path)],[]))
        print x
        tot = tot + x
    print 'Total files is %d'%tot


'''
#2015-10-2 20:44:43 doing
# __moveP1():
#separate diff files from each action folder
# sender folder : ./files/Bathroom/
# sendee folder : /Bathroom_correct/
                 # /Bathroom_1/
                 # /Bathroom_2/
according file: ./experiment/2/soundAnalysis/Bathroom.dat

vs d:\class\Semester5\research\ADLRecorder\code\python\SDL\experiment\2\soundAnalysis\Bus.dat
'''
def __moveP1(actionName):
    m_filename = 'd:\class\Semester5\\research\ADLRecorder\code\python\SDL\experiment\\2\soundAnalysis\\'+actionName+'.dat'
    fp = open(m_filename,'r')
    bufferl = fp.readlines()
    folderName = actionName.replace(' ','')

    def __actionPrediction(m_filename):
        actionPredicted = set()
        pwd = os.getcwd();
        for line in bufferl:
            if ';' in line:
                data_s = line.strip('\n').split(';')
                data_s1 = data_s[1].replace(' ','')
                actionPredicted.add(data_s1)
                path = str(pwd) +'\\files\\'+str(folderName)+'\\'+str(folderName)+'_'+str(data_s1)
                #print path
                if not os.path.exists(path):
                    os.mkdir(path)
                shutil.move(pwd+'\\files\\'+folderName+'\Living_'+data_s[0]+'.mp3', path+'\\')
        #print actionPredicted
        return actionPredicted

    actionPredicted = __actionPrediction(m_filename)

    fp.close()
    return actionPredicted


if __name__=="__main__":
    actionList = [\
    #'Working on PC at home', 'Walking at home',\
    'Washing in bathroom',\
    'Washing dishes',\
    'Bathroom',\
    'Cooking',\
    'Bus',\
    'Driving',\
    'Walking outside',\
    'Waiting for a bus']
    #step1
    #movePW(actionList)
    #step2
    #numberFilesInFolder(actionList)
    #print actionList[0]
    #__moveP('Bus')

    '''
    for action in actionList:
        __moveP1(action.replace(' ',''))

    __moveP1(actionList[4].replace(' ',''))
    '''






