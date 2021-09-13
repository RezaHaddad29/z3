# from z3 import *


# # Use I as an alias for IntSort()
# I = IntSort()
# # A is an array from integer to integer
# A = Array('A', I, I)
# x = Int('x')

# s = Solver()
# Store(A,0,29)
# s.check()

# print(A[0])


# A = Array('A', IntSort(), IntSort())
# x, y = Ints('x y')
# print(solve(A[x] == x, Store(A, x, y) == A, x != y))





# Color, (red, green, blue) = EnumSort('Color', ('red', 'green', 'blue'))

# print (simplify(green == green))

# c = Const('c', Color)
# solve(c != green, c != blue)



# Color, (red, green, blue) = EnumSort('Color', ['red', 'green', 'blue'])

# nElems = Color.num_constructors();

# s = Solver()

# vs = [Const("v%d" % i, Color) for i in range(nElems)]
# for i in range(nElems):
#     s.add(vs[i] == Color.constructor(i)())

# print(s.check())
# print(s.model())

# A = Array('A', IntSort(), ArraySort(IntSort(), IntSort()))
# x, y = Ints('x y')
# s = Solver()
# s.add(Store(A,0,(0,2)))
# s.add(x = A[0][0])
# print(A[x][y])

# a = int(input())
# b = int(input())
# r = int(input())

# f = z3.Function('f',IntSort(),IntSort(),IntSort())
# s= Solver()
# x,y=Ints('x y')
# s.add(x == a)
# s.add(y == b)
# s.add(ForAll([x,y],z3.Or(f(x,y)==x+y, f(x,y)==x*y)))
# s.add(f(x,y)==r)
# s.check()
# print(s.model())



# s = Solver()

# Q = [Int(f'Q{i}') for i in range(100)]

# costs = ""

# s.add(Distinct(Q[0],Q[1],Q[2]))

# for i in range(100):
#     s.add(Or(Q[i] == 1500,Or(Q[i] == 100,Q[i] == 25)))
#     if(i == 99):
#         costs +=f"Q[{i}] == 10000"
#     else:     
#         costs +=f"Q[{i}] + "

# s.add(eval(costs))
# s.check()
# print(s.model())


