def SecondLargest(L):
    if not L:
        return None
    else:
        max=L[0]
        smax=None
        for i in range(1,len(L)):
            if L[i]>max:
                smax=max
                max=L[i]
            elif L[i]>smax and L[i]<max:
                smax=L[i]
        return smax

print(SecondLargest([2,2,2]))