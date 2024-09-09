def RemoveDuplicates(L,n):
    siz=1
    for i in range(1,len(L)):
        if L[siz-1]!=L[i]:
            L[siz]=L[i]
            siz+=1
    return siz
print(RemoveDuplicates([10,15,20,20,30,30,30,30],7))
    