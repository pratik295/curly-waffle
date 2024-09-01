class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii = [ord(char) for char in s]
    

        score = sum(abs(ascii[i] - ascii[i + 1]) for i in range(len(ascii) - 1))
    
        return score
