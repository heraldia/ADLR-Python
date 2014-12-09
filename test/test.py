var = 123445
s= locals()['var']
s2=vars()['var']

print s,s2

print "-"*60
def cube(x): return x*x*x
a = map(cube, range(1, 11))
print a

def cube1(x) : return x + x
print map(cube1 , "abcde")


foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print [x * 2 + 10 for x in foo]
print [x for x in foo if x % 3 == 0]
fs = [(lambda n, i=i : i + n) for i in range(10)]
print fs
print fs[3](4)

print
def create_multipliers():
    return [lambda x, i=i : i * x for i in range(5)]

for multiplier in create_multipliers():
    print multiplier(2)
