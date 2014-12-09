import random
import linecache
#from random import shuffle

path = 'cmd.dat'
with open(path) as f:
    linecount = sum(1 for _ in f)

shuffled = random.shuffle(range(linecount))

print shuffled
print linecount
#typeof(shuffled)
#shuffled = int(shuffled)
'''
with open(path + '.shuffled', 'w') as f:
    for i in shuffled:
        f.write(linecache.getline(path, i))
'''
