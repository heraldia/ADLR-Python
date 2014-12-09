import os

os.system("python db.py > result.txt")
os.system("python delDuplicates.py")
os.system("del result.txt")
