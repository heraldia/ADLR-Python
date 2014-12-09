import os

os.system("del *.dat")
os.system("python db.py > wifiFingerPrinting.txt")

os.system("python test4.py > cmd.dat")
os.system("shuffleP1.py")
#os.system("del wifiFingerPrinting.txt")
#os.system("del result.txt")
#os.system("del cmd.dat")
os.system("python fileDistribute.py")
#os.system("del cmd1.dat")
