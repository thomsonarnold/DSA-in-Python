lst=[10,41,30,15,80]
Odd=[]
Even=[]
for i in lst:
    if i%2==0:
        Even.append(i)
    else:
        Odd.append(i)
print(Even,Odd)