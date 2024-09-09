def median(A,N):
    A.sort()
    if N%2!=0:
        return A[N//2]
    elif N%2==0:
        mid1=A[N//2]
        mid2=A[N//2-1]
        return (mid1+mid2)//2
def mean(A,N):
    return sum(A)//N
print(median([2,8,3,4],4))
print(mean([2,8,3,4],4))