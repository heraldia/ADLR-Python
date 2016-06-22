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
    djv.fingerprint_directory("mp3", [".wav"])

    #print djv.db.get_num_fingerprints()
    #print "----------------------------17---------"

    fp = open('result'+'.dat','w+')
    # Recognize audio from a file

    prefix ='../sdl/miniFiles/'

    start =  time.clock()
    totalNumSong = 0
    for root, dirs, files in os.walk(prefix):
        for dirx in dirs:
            fp.write('%s\n'%dirx)
            for filename in glob.glob(os.path.join(prefix, dirx)+'/*.wav'):
                #print filename
                filenamex= os.path.basename(filename).replace('.wav','')
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
    fp.write("Prediction time duration: %f seconds\n"%(end-start))
    fp.write("Total number of predicted songs: %d \n"%totalNumSong)
    fp.write("Prediction duration for per song: %f seconds\n"%(float(end-start)/float(totalNumSong)))
    fp.close()


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

if __name__ == '__main__':
    import os
    num = 4
    __result_folder = '.\\result\\%s\\'%num
    if os.path.exists(__result_folder ):
        os.system('mkdir %s'%__result_folder)

    os.system('move *.dat %s'%__result_folder)
    __main1()

