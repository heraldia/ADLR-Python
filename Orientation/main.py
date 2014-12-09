import os
from freAnaly import *

if __name__ == "__main__":
    os.system("python db.py > activityList1.txt")
    os.system('python rep1ace.py')
    os.system("python generateDatFile.py > result.txt")
    os.system("del activityList1.txt")

    os.system("copy result.txt Report_distri.dat")

    #freAnaly = FreAnaly()
    #freAnaly.generaAllFileAngle()
    os.system("python freAnaly.py")
    #os.system("del result.txt")
