class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        r=nums[:]
        nums.extend(r)
        return nums
        
