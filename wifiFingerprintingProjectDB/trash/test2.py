# File: test2.py
# step2
# python  test2.py > cmd1.dat

import random
file = open("cmd.dat")
for line in file:
   rand = random.randint(1,400)
   line = str(rand) + '\t' +line
   print line[:-1]
file.close()

