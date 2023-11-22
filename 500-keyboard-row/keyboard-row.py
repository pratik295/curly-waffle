class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        str1=set("qwertyuiop")
        str2=set("asdfghjkl")
        str3=set("zxcvbnm")
        result=[]
        for word in words:
            new_word=word.lower()
            if all( char in str1 for char in new_word):
                result.append(word)
            if all( char in str2 for char in new_word):
                result.append(word)
            if all( char in str3 for char in new_word):
                result.append(word)
        return result

        