class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        arr=""
        for i in range(len(words)):
            word=words[i]
            arr+=(word[0])
        return arr==s
        

