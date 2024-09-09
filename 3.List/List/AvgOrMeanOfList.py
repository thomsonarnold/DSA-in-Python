lst=list(map(int,input().split()))
avg=sum(lst)/len(lst)
print(round(avg,2))

#or

sum=0
for i in lst:
    sum+=i
avg1=sum/len(lst)
print(round(avg1,2))