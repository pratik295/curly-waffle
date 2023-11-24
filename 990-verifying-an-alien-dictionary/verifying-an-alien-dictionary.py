class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashi={char:i for i,char in enumerate (order)}

        def solve(word1,word2):
            i=0
            j=0
            while i<len(word1) and j<len(word2):
                if hashi[word1[i]]<hashi[word2[j]]:
                    return True
                if hashi[word1[i]]>hashi[word2[j]]:
                    return False
                i+=1
                j+=1
            return i==len(word1)

        for i in range(1,len(words)):
            if not solve(words[i-1],words[i]):
                return False
        return True
                