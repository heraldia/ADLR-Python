import os

os.system("python db.py > activityList.txt")
os.system("python generateDatFile.py")

os.system("copy result.txt Report_distri.dat")
#os.system("del result.txt")
