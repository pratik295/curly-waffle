class Solution:
    def climbStairs(self, n: int) -> int:
        dp={1:1,2:2}

        def solve(n):
            if n in dp:
                return dp[n]
            ans=solve(n-1)+solve(n-2)
            dp[n]=ans
            return ans 
        return solve(n)