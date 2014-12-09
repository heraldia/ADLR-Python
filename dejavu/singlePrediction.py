from dejavu import Dejavu
import warnings
import json
import os
import getopt, sys

warnings.filterwarnings("ignore")

#global _DEBUG

#_DEBUG=False
#_XDEBUG=False
#_DEBUG=True

# load config from a JSON file (or anything outputting a python dictionary)
with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

# create a Dejavu instance
djv = Dejavu(config)

# Recognize audio from a file
from dejavu.recognize import FileRecognizer
filename = "20141106_204003"
#filename = sys.argv[1]
import globP
if globP._XDEBUG == True:
    import pdb
    pdb.set_trace()
txtFileName = 'songList.txt'
prefix ='./mp3t/Living_'
suffix ='.mp3'
fullFilename=prefix+filename+suffix
#print fullFilename
if os.path.exists(fullFilename):
    song = djv.recognize(FileRecognizer, fullFilename)
    if not song is None:
        print "36 --  %s \t %s "%(filename, song['song_name'] )
    else:
        print "38 --  %s \t None "%(filename)

print song
