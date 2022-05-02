nums = [3,1,2,4]
l=[]
for i in nums:
    if(i%2==0):
        l.append(i)
for j in nums:
    if(j%2!=0):
        l.append(j)
print(l)
