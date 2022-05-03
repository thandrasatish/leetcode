class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        temp = nums.copy()
        temp.sort()
        if temp==nums:
            return 0
        # print(temp)
        # print(nums)
        for i in range(0,len(temp)):
            if temp[i]==nums[i]:
                pass
            else:
                lower = i
                break
        nums.reverse()
        temp.reverse()
        # print(lower)
        for i in range(0,len(temp)):
            if temp[i]==nums[i]:
                pass
            else:
                higher = i
                break
        # print(higher)
        return len(temp)-higher-lower
