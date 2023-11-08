class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_x=str(x)
        l=0
        r=len(new_x)-1
        while l<=r:
            if new_x[l]!=new_x[r]:
                return False
            l+=1
            r-=1
        return True