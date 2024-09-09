n=int(input())

def Sieve(n):
    for i in range(2,n+1):
        if isPrime(i):
            print(i,end=',')
    
    
def isPrime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

