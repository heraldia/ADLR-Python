import re
import os


os.system('del *.dat')

#filenames = ['Dinner', 'Cooking', 'Washing', 'Bathroom', 'Working',\
#        'Lunch','Breakfast', 'Eating', 'Midnight', 'Music']
activity_set = set()
#for filename in filenames:
f1 = file('activityPrediction.txt', 'r')
patt = re.compile(r'^[2]', re.I|re.U|re.X)
#patt = re.compile(r'^[0-9]', re.I|re.U|re.X)
#lineCounter = 0
for line in f1.readlines():
    #lineCounter +=1
    if not patt.match(line) :
        continue
    else:
        sTr = line.split('\t')
        #print sTr
        strsub = sTr[1].strip()
        if  strsub != '':
            activity_set.add(strsub)
        f1.close()

for filename in activity_set:
    f1 = file('activityPrediction.txt', 'r')
    fresult = file(filename+'.dat', 'w')
    for line in f1.readlines():
        if not patt.match(line) :
            continue
        else:
            if filename in line:
                fresult.write(line);
    fresult.close()
    f1.close()

print activity_set

#os.system('del result.txt')
