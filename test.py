from z3 import *


x = BitVec('x', 8)

y = BitVec('y', 8)
h = BitVec('h',8)
slow = x * 2
faster = x << h

s = Solver()
s.add(ForAll([x], slow == faster))
s.check()
print(s.model())
