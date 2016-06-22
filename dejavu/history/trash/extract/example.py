from dejavu import Dejavu
import warnings
import json
import os
import time

warnings.filterwarnings("ignore")

global _DEBUG

#_DEBUG=False
_XDEBUG=False
_DEBUG=True

# load config from a JSON file (or anything outputting a python dictionary)
with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

# create a Dejavu instance
djv = Dejavu(config)

# Fingerprint all the mp3's in the directory we give it
djv.fingerprint_directory("seed", [".mp3"])

print djv.db.get_num_fingerprints()
print "----------------------------17---------"
print "Filename \t\t ActualActivity \t\t Prediction \t\t PredictionByHumanEar "

#f1 = open("activityPrediction.txt", "w")

start =  time.clock()
# Recognize audio from a file
from dejavu.recognize import FileRecognizer
#filename = "Living_20141017_114206.mp3"
#import glob
if _XDEBUG == True:
    import pdb
    pdb.set_trace()
#for filename in glob.glob(r'./mp3t/*1004*.mp3'):
#for filename in glob.glob(r'./mp3t/Living_20141017_114206.mp3'):
txtFileName = 'songList.txt'
prefix ='./mp3t/'
totalNumSong = 0
f1 = file(txtFileName, 'r')
for line in f1.readlines():
    filename='Living_'+line[0:15]+'.mp3'
    fullFilename=prefix+filename
    if os.path.exists(fullFilename):
        totalNumSong += 1
        song = djv.recognize(FileRecognizer, fullFilename)
        if not song is None:
            print "%s\t%s\t%s"%(filename[7:-4], line[15:-2], song['song_name'])
        else:
            print "%s\t%s\tNone"%(filename[7:-4],line[15:-2])
        #print song['song_name']
    else:
        continue

end=time.clock()
print "----------------------------60---------"
print "Prediction time duration: %f "%(end-start)
print "Total number of predicted songs: %d "%totalNumSong
#print "Prediction duration for per song: %f "%float(end-start)/float(totalNumSong)


print "----------------------------60-- dbInfor()-------"
from dbRefresh import dbInfor
dbInfor()
