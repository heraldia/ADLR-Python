# File: test1.py
# step1
# python test1.py > cmd.dat

file = open("g:/class/Semester5/research/ADL Recorder/code/python/wifiFingerprintingDB/result.txt")
for line in file:
    sStr1 = line.split(' ')
    rStr = sStr1[0]
    rStr += '\t'
    for i in range(1,9):
        rStr += sStr1[i]
        rStr += '\t'
    print rStr[:-2]
file.close()



