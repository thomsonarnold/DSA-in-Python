# def CheckSorted(L):
#     if len(L)<=1:
#         return True
#     for i in range(len(L)):
#         for j in range(1,len(L)):
#             if L[i]>L[j]:
#                 return False
#             break
#         return True

# print(CheckSorted([10,20,30,30,40]))
     

def CheckSorted(L):
    if len(L)<=1:
        return True
    else:
        s=L[0]
        for i in range(1,len(L)):
            if L[i]<s:
                return False
        return True
print(CheckSorted([10,10,10]))
