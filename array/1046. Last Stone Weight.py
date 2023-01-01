class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones)>1):
            y=max(stones)
            p=[]
            for i in stones:
                p.append(i)
            p.sort()
            x=p[-2]
            if(x<=y):
                if(x==y):
                    stones.remove(x)
                    stones.remove(y)
                else:
                    y1=stones.index(y)
                    stones[y1]=stones[y1]-x
                    stones.remove(x)
        if(len(stones)>0):
            return stones[0]
        else:
            return 0
        
