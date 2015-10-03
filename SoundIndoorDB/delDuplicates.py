from sets import Set

#2015-09-27 17:42:53
def delDuplicates(filenames):

    for filename in filenames:

        file(filename+".txt","w").writelines( Set(file(filename+'.dat', "r").readlines()) )

def countP(filenames):
    total = 0
    for filename in filenames:
        print filename,':',
        count = len(open(filename+'.txt','rU').readlines())
        print count
        total = total+count
    print "Total number of audio files with annotation is %d ."%total


