import os

os.system("python db.py > result.txt")
os.system("python delDuplicates.py")
os.system("python delOutdoor.py")
os.system("python rep1ace.py")
os.system("python addTagNum.py > test.dat")


#os.system("averageP.py")


#os.system('pause')
#os.system('del result.txt')
#os.system('del result2.txt')
