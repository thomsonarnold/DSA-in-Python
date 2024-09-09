# def Reverse(L):
#     R=L.reverse()
#     return R
# print(Reverse([10,20,30,40]))

# def Reverse(L):
#     L.reverse()
#     return L

# print(Reverse([10,20,30,40]))


# def reverse_list(L):
#     l_len = len(L)
#     l_half_len = len(L)//2
#     for i in range(l_half_len):
#         temp = L[l_len - i - 1]
#         L[l_len - i - 1] = L[i]
#         L[i] = temp
#     return L

# reverse_list([1,2,3,4,5,6,7])

def ReverseList(L):
    s=0
    e=len(L)-1
    while s < e:
        L[s],L[e]=L[e],L[s]
        s+=1
        e-=1
    return L
print(ReverseList([1,2,3,4,5,6,7,8,9]))


