
import math
def QuadraticEquationRoots(a,b,c):
    # a=int(input())
    # b=int(input())
    # c=int(input())

    dis=b**2 - 4*a*c
    if dis<0:
        return -1
    
    sqrtdis=math.sqrt(dis)

    root1=math.floor((-b + sqrtdis)/(2*a))
    root2=math.floor((-b - sqrtdis)/(2*a))
    
    if root1 >= root2:
        return[root1,root2]
    else:
        return [root2,root1]

print(QuadraticEquationRoots(1,-7,12))