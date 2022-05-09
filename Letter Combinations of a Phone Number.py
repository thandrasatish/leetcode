class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lis = [int(x) for x in digits]
        let = {2: ['a', 'b', 'c'],
               3: ['d', 'e', 'f'],
               4: ['g', 'h', 'i'],
               5: ['j', 'k', 'l'],
               6: ['m', 'n', 'o'],
               7: ['p', 'q', 'r', 's'],
               8: ['t', 'u', 'v'],
               9: ['w', 'x', 'y', 'z']}
        out = []
        for d in lis:
            if len(out) == 0:
                out = let[d]
            else:
                out = [a+b for a in out for b in let[d]]
        return (out)
