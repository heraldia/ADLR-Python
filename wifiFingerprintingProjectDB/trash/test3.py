# File: test3.py
# step4
# python  test3.py > cmd2.dat

file = open("cmd.dat")
for line in file:
    i = line.index('\t')
    #print i
    print line[i+1:-1]
file.close()

