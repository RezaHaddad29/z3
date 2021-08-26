from z3 import *


x1 = Int('x1')
x2 = Int('x2')
x3 = Int('x3')
x4 = Int('x4')
x5 = Int('x5')
x6 = Int('x6')
x7 = Int('x7')
x8 = Int('x8')
x9 = Int('x9')

s = Solver()

for i in range(1,10):
    s.add(eval("x{0} >0".format(i)))
    s.add(eval("x{0} <10".format(i)))
    for j in range(i,10):
        if i!=j:
            r = "x{0} != x{1}".format(i,j)
            s.add(eval(r))
    
s.add(x1+x2+x3+x4 ==17)
s.add(x4+x5+x6+x7 ==17)
s.add(x7+x8+x9+x1 ==17)
s.check()
print(s.model())
