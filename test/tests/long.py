l = 2L
print l
print type(l)

t = 1L
for i in xrange(150):
    t *= l
    print t, repr(t)

def test(a, b):
    print a, b
    print a + b, b + a, a.__add__(b), b.__add__(a)
    print a - b, b - a, a.__sub__(b), b.__sub__(a)
    print a * b, b * a, a.__mul__(b), b.__mul__(a)
    print a / b, b / a, a.__div__(b), b.__div__(a)
    print repr(a), repr(b), a < b, a > b, a <= b, a >= b, a == b, a != b
    # print a ^ b, a | b, a & b


print 1L / 5L
print -1L / 5L
print 1L / -5L
print -1L / -5L

for a in [-5, -1, 1, 5, -2L, -1L, 1L, 2L]:
    for b in [-5, -1, 1, 5, -2L, -1L, 1L, 2L]:
        test(a, b)

print (2L).__rdiv__(-1)
print (2L).__rdiv__(-1L)
print (-2L).__rdiv__(1L)
print (-2L).__rdiv__(1)

print (1L) << (2L)
print (1L) << (2)
try:
    print (1L) << (-1L)
except ValueError, e:
    print e
try:
    print (1L) << (-1)
except ValueError, e:
    print e

print long("100", 16)
print long("100", 10)
print long("100", 26)

print type(hash(1L))
print hash(1L) == hash(2L)

# Testing long.__new__:
class C(long):
    def __init__(self, *args):
        print "C.__init__, %d args" % len(args)

class D(object):
    def __init__(self, n):
        self.n = n

    def __long__(self):
        return self.n

for a in (False, True, 2, 3L, D(4), D(C(5)), D(False)):
    i = long.__new__(C, a)
    print type(i), i, type(long(a))

try:
    long.__new__(C, D(1.0))
except TypeError, e:
    print e

class I(long):
    pass

x = long(D(C()))
print type(x)

x = I(D(C()))
print type(x)

print type(long(C()))
