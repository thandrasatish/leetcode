from collections import Counter
import math
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        x=Counter(tasks)
        res=0
        for i in x:
            if(x[i]==1):
                return -1
            res=res+int(math.ceil(x[i]/3))
        return res
