def satish(nums):
    stack=[]
    curr=nums[0]
    for i in nums[1:]:
        while(stack and i>=stack[-1][0]):
            stack.pop()
        if(stack and i>stack[-1][1]):
            return True
        stack.append([i,curr])
        curr = min(curr,i)
    return False
        
nums = [1,2,3,4]
print(satish(nums))
