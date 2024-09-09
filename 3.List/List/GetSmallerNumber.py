# # def smaller(A,x):
# #     Small=[]
# #     for i in A:
# #         if i<x:
# #             Small.append(i)
# #     return Small
# # A=[8,100,56,45,2,1,34,69,51]
# # x=60
# # print(smaller(A,x))
        

# def smaller(A,x):
#     return [i for i in A if i<x]
# A=[10,20,30,40,50]
# x=40
# print(smaller(A,x))

def OddEven(A):
    Odd=[i for i in A if i%2!=0]
    Even=[ i for i in A if i%2==0]

    return Odd,Even
print(OddEven([10,20,2,5,3,67,45,86]))