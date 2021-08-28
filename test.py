from z3 import *


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



s = Solver()
R = [[Int(f"R{i}_C{j}") for j in range(9)] for i in range(9)]

for r in R:
    for c in r:
        s.add(c >= 1)
        s.add(c <= 9)

for r in R:
    s.add(Distinct(r))

for i in range(9):
    l = []
    for j in range(9):
        l.append(R[j][i])
    s.add(Distinct(l))

for row in range(0,7,3):
    for k in range(0,7,3):
        box = []
        for i in range(row,row+3):
            for j in range(k,k+3):
                box.append(R[i][j])
        s.add(Distinct(box))

pzl = ((0,0,0,0,9,4,0,3,0),
            (0,0,0,5,1,0,0,0,7),
            (0,8,9,0,0,0,0,4,0),
            (0,0,0,0,0,0,2,0,8),
            (0,6,0,2,0,1,0,5,0),
            (1,0,2,0,0,0,0,0,0),
            (0,7,0,0,0,0,5,2,0),
            (9,0,0,0,6,5,0,0,0),
            (0,4,0,9,7,0,0,0,0))

pzl_ = [ If(pzl[i][j] == 0,
                  True,
                  R[i][j] == pzl[i][j])
               for i in range(9) for j in range(9) ]
s.add(pzl_)
s.check()

print(pzl_)


m = s.model()
r = [ [ m.evaluate(R[i][j]) for j in range(9) ]
        for i in range(9) ]
print_matrix(r)
