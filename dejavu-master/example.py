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


def main(action):
    # create a Dejavu instance
    djv = Dejavu(config)

    # Fingerprint all the mp3's in the directory we give it
    djv.fingerprint_directory("mp3", [".mp3"])

    #print djv.db.get_num_fingerprints()
    #print "----------------------------17---------"

    fp = open(action+'.dat','w+')
    # Recognize audio from a file
    prefix ='..\sdl\%s'%action
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
    fp.write("----------------------------60---------")
    fp.write("Prediction time duration: %f \n"%(end-start))
    fp.write("Total number of predicted songs: %d \n"%totalNumSong)
    fp.write("Prediction duration for per song: %f \n"%(float(end-start)/float(totalNumSong)))
    fp.close()

if __name__ == '__main__':
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
    import os
    num = 1
    os.system('mkdir .\\result\\%s\\'%num)
    os.system('move *.dat result\\%s\\'%num)
    for action in actionList:
        main(action)

