class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        l1=[]
        for i in range(len(accounts)):
            r=sum(accounts[i])
            l1.append(r)
        return max(l1)
        
