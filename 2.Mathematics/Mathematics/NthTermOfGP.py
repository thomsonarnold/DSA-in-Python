import math
def GP(A,B,n):
    cr=B/A
    return math.floor(A*(cr**(n-1)))
print(GP(1,2,5))