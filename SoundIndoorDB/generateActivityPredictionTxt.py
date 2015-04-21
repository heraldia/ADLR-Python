import glob

infile = '* result.txt'
outfile = 'activityPrediction.txt'


def generateTxt():
    f2 = open(outfile,'w')
    for filename in\
        glob.glob(infile):
        #glob.glob(r'/.*result.txt'):
        if not filename == 'all result.txt':
            #print filename
            with open(filename) as f:
                for line in f:
                    prefix = line[0:4]
                    print prefix
                    if prefix == '2014':
                        f2.write(line)
                        print line
    f2.close()



if __name__=="__main__":
    #generateTxt()
    import os
    os.system("copy activityPrediction.txt g:\\class\\Semester5\\research\\ADLRecorder\\code\\python\\SoundActivityAnalysis\\activityPrediction.txt")

