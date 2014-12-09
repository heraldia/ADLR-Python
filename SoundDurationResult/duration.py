import os
import glob


def mbmGetFLVDuration (directory):
    for file in glob.glob(directory):
        print file
        os.system ("ffmpeg -i "+file+" 2>&1 | grep 'Duration' | cut -d ' ' -f 4 | sed s/,//")

if __name__=="__main__":
    directory = '../Music/*.mp3'
    mbmGetFLVDuration(directory)
