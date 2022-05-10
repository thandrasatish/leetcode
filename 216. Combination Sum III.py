class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def helper(target, k, index, curr):
            if k == 0:
                if target == 0:
                    res.append(curr.copy())
                return
            for i in range(index, 10):
                if target >= i:
                    curr.append(i)
                    helper(target-i, k-1, i+1, curr)
                    curr.pop()
            return
        helper(n, k, 1, [])
        return res
