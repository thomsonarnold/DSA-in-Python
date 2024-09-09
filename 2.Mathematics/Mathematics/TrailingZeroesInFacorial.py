# def TrailingZeroes(n):
#     if n<0:
#         return -1
#     count=0
#     i=5
#     while(n//i>=1):
#         count+=n//i
#         i*=5
#     return count
# if __name__ == "__main__":
#     n = 100
#     print(f"Count of trailing 0s in {n}! is {TrailingZeroes(n)}")


def TrailingZeroes(n):
    count =0
    fact=1
    for i in range(2,n+1):
        fact=fact*i
    while(fact>0):
        if fact%10==0:
            count+=1
        else:
            break
        fact//=10

    return count
if __name__ == "__main__":
    n = 15
    print(f"Count of trailing 0s in {n}! is {TrailingZeroes(n)}")