import os

os.system("python db.py > activityList.txt")
os.system("python delDuplicates.py")
os.system("del result.txt")
