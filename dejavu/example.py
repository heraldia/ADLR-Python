import warnings
import json
warnings.filterwarnings("ignore")
import time
import glob

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)


def test1():
    actionList=[\
    #'Bathroom',\
    #'Bus',\
    'Cooking',\
    'Driving',\
    'Waitingforabus',\
    'Walkingoutside',\
    'Washingdishes',\
    'Washinginbathroom'\
    ]
    for action in actionList:
        __main(action)

def __main(action):
    # create a Dejavu instance
    djv = Dejavu(config)

    # Fingerprint all the mp3's in the directory we give it
    djv.fingerprint_directory("mp3", [".wav"])

    #print djv.db.get_num_fingerprints()
    #print "----------------------------17---------"

    fp = open(action+'.dat','w+')
    # Recognize audio from a file
    #prefix ='..\sdl\%s'%action
    prefix ='mp3\%s'%action
    files = prefix +'\*.mp3'
    totalNumSong = 0
    start =  time.clock()
    for filename in glob.glob(files):
        #print filename
        filenamex= filename.split('\\')[-1]
        filenamex=filenamex[7:-4]
        song = djv.recognize(FileRecognizer, filename)
        totalNumSong += 1
        if not song is None:
            txtBuffer = "%s;%s"%(filenamex, song['song_name'])
        else:
            txtBuffer =  "%s;None"%(filenamex)
        fp.write(txtBuffer+'\n')
        print txtBuffer

    end=time.clock()
    fp.write("----------------------------60---------\n")
    fp.write("Prediction time duration: %f \n"%(end-start))
    fp.write("Total number of predicted songs: %d \n"%totalNumSong)
    fp.write("Prediction duration for per song: %f \n"%(float(end-start)/float(totalNumSong)))
    fp.close()


def __main1():
    # create a Dejavu instance
    djv = Dejavu(config)

    # Fingerprint all the mp3's in the directory we give it
    djv.fingerprint_directory("seed", [".wav"])

    #print djv.db.get_num_fingerprints()
    #print "----------------------------17---------"

    fp = open('result'+'.dat','w+')
    # Recognize audio from a file

    prefix ='mp3'

    start =  time.clock()
    totalNumSong = 0
    rightNum = 0
    missNum = 0
#     for root, dirs, files in os.walk(prefix):
#         for dirx in dirs:
#             fp.write('%s\n'%dirx)
    print "-------------------------------------"
    fp.write("--Recognizing-----------------------------------\n")
    for filename in glob.glob(prefix+'/*.wav'):
        #print filename
#         filenamex= os.path.basename(filename).replace('.wav','')
        song = djv.recognize(FileRecognizer, filename)
        totalNumSong += 1
        if not song is None:
            txtBuffer = "%s; %s"%(filename, filter(str.isalpha, song['song_name']))
            if filename[5:7] in filter(str.isalpha, song['song_name']):
                rightNum += 1
        else:
            txtBuffer =  "%s; None"%(filename)
            missNum +=1 
        fp.write(txtBuffer+'\n')
        print txtBuffer
        

    end=time.clock()
    
    fp.write("--Performance-----------------------------------\n")
    fp.write("Prediction time duration: %f seconds\n"%(end-start))
    fp.write("Total number of predicted songs: %d \n"%totalNumSong)
    fp.write("Prediction duration per song: %f seconds\n"%(float(end-start)/float(totalNumSong)))
    fp.write("Correct rate: %f %% \n"%(float(rightNum)/float(totalNumSong)*100))
    fp.write("No result rate: %f %%\n"%(float(missNum)/float(totalNumSong)*100))
    fp.close()


if __name__ == '__main__':
    import os
    num = 4
    __result_folder = '.\\result\\%s\\'%num
    if not os.path.exists(__result_folder ):
        os.system('mkdir %s'%__result_folder)

    os.system('move *.dat %s'%__result_folder)
    __main1()

