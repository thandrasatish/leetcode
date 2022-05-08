class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def flat(nestedList):
            res = []
            for i in nestedList:
                if i.isInteger():
                    res.append(i.getInteger())
                else:
                    res.extend(flat(i.getList()))
            return res
        
        self.flatList = flat(nestedList)
    
    def next(self) -> int:
        return self.flatList.pop(0)
        
    def hasNext(self) -> bool:
        return len(self.flatList) > 0
