def getmax(l):
    if not l:
        return None
    max1=l[0]
    for i in range(1,len(l)):
        if l[i]>max1:
            max1=l[i]
    return max1
print(getmax([10,5,20,8]))

