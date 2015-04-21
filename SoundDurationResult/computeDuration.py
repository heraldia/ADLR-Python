import re
import os

os.system ("python duration.py > soundDuration.txt")

#def computeDuration()
f1 = file('soundDuration.txt', 'r')
fresulttrain = file('computeDuration.txt', 'w')
patt = re.compile(r'^[0-9]', re.I|re.U|re.X)
totalSecond = 0

for line in f1.readlines():
    if patt.match(line):
        duration = line.split(':')
        hour = int(duration[0])
        minute = int(duration[1])
        #second = round(float(duration[2]),0)
        second = float(duration[2])

        duration_in_seconds = hour*3600 + minute*60 + second*1
        totalSecond += duration_in_seconds
        duration_in_seconds = str(duration_in_seconds)
        fresulttrain.write(duration_in_seconds+'\n')

f1.close()
fresulttrain.write('TotalSeconds = %s'%totalSecond+'\n')
mHour =int( totalSecond / 3600)
mMinute =int( totalSecond % 3600 /60)
mSecond = totalSecond % 3600 % 60
fresulttrain.write('TotalDuration = %s : %s : %s'%(mHour,mMinute,mSecond)+'\n')
fresulttrain.close()

