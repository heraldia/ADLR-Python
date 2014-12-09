def factorial(n):
    if n == 0 or n == 1: return 1
    else: return (n * factorial(n - 1))

print factorial(6)

print "-" * 40
def add(n):
    if n <= 0: return 0
    if n > 0: return n + add(n - 1)
print add(100)

print sum(i*i for i in range(10))

for i in xrange(10):
    print i

def generator1():
    yield 'first'
    yield 'second'
    yield 'third'

gen=generator1()
print gen.next()
print gen.next()
print gen.next()
#print gen.next()


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1

for i in fab(6):
    print i,

isgeneratorfunction(fab)
