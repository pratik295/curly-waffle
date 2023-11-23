class Solution:
    def romanToInt(self, s: str) -> int:
        hashi={'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        nume=0
        i=0

        while i<len(s)-1:
            ch=""
            ch+=s[i]+s[i+1]
            if ch in hashi:
                nume+=hashi[ch]
                i+=2
            else:
                nume+=hashi[s[i]]
                i+=1
        
        if i==len(s)-1:
            nume+=hashi[s[i]]
        return nume