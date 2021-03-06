# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        b = {}
        ans = 0
        for i in nums:
			# If there is num in table and is not used
            if k - i in b and b[k - i] > 0:
                ans += 1
                b[k - i] -= 1  # used
            elif i not in b:
                b[i] = 1
            else:
                b[i] += 1
        
        return ans
      
      

      
      
#  Example 1:

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
# Example 2:

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.
