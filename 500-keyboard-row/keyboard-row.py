class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        str1=set("qwertyuiop")
        str2=set("asdfghjkl")
        str3=set("zxcvbnm")
        result=[]
        for word in words:
            new_word=set(word.lower())
            if new_word<=str1 or new_word<=str2 or new_word<=str3:
                result.append(word)
            
        return result

        