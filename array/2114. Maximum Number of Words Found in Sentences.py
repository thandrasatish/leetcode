class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        l1=[]
        for i in range(len(sentences)):
            l1.append(len(sentences[i].split()))
        return max(l1)
        
