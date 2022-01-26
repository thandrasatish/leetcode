class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        mid=len(nums)//2
        r=nums[:mid]
        r1=nums[mid:]
        l1=[]
        for i in range(len(r)):
            l1.append(r[i])
            l1.append(r1[i])
        return l1
        
        
