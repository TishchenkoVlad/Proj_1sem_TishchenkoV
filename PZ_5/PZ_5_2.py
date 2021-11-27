import math
sqrt = math.sqrt(3/4)

def TrianglePS(a):
    P = 3 * a
    S = a ** 2 * sqrt
    return P, S

res = TrianglePS(int(input()))
print(res)

print(TrianglePS(res[0]))

print(TrianglePS(res[1]))
