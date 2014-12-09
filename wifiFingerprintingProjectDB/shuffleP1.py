import random
with open('cmd.dat','r') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()
with open('cmd1.dat','w') as target:
    for _, line in data:
        target.write( line )
