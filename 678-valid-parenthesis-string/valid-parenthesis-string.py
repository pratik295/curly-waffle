class Solution:
    def checkValidString(self, s: str) -> bool:
        stack=[]
        star=[]
        for ind,char in enumerate(s):
            if char=='(':
                stack.append(ind)
            elif char==')':
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False 
            else:
                star.append(ind)
        
        while stack and star:
            if stack[-1]>star[-1]:
                return False
            stack.pop()
            star.pop()
        return len(stack)==0
