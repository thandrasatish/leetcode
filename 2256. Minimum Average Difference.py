nums = [2,5,3,9,5,3]
N=len(nums)
left=0
right=sum(nums)
minindex=0
minn= 10**20
for i in range(N):
    left +=nums[i]
    right -=nums[i]
    if(i+1 == N):
        r=abs(left//(i+1))
    else:
        r=abs(left//(i+1)-right//(N-i-1))
    if(r<minn):
        minn=r
        minindex = i
print(minindex)
