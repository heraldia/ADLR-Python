# http://bbs.csdn.net/topics/390697894

pswpath = "wifiDbTest.dat"
tmppath = "wifiDbTest1.dat"
tmp_file = open(tmppath, "w")
f = open(pswpath, "r")
lines = f.readlines()
for line in lines:
    if line.find('Walking') > -1:
        continue
    if line.find('NULL') > -1:
        continue
    if line.find('Class') > -1:
        continue
    if line.find('Testing') > -1:
        continue
    if line.find('Bus') > -1:
        continue
    if line.find('Library') > -1:
        continue
    if line.find('library') > -1:
        continue
    if line.find('smhlab') > -1:
        continue
    if line.find('Exercise') > -1:
        continue
    if line.find('Waiting for a bus') > -1:
        continue
    if line.find('Biking') > -1:
        continue
    if line.find('Driving') > -1:
        continue
    if line.find('dine') > -1:
        continue
#    if line.find('Biking') > -1:
#        continue
#    if line.find('Biking') > -1:
#        continue
    if line.find('0 0 0') > -1:
        continue
    tmp_file.write(line)
f.close()

tmp_file.close()
