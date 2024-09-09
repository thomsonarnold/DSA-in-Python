def LeftRotate(L):
    first=L[0]
    for i in range(len(L)-1):
        L[i]=L[i+1]
        L[-1]=first
    return L
print(LeftRotate([10,20,30,40]))