class Solution:
    def tribonacci(self, n: int) -> int:
        dp={0:0,1:1,2:1}
        def solve(n):
            if n in dp:
                return dp[n]
            ans= solve(n-1)+solve(n-2)+solve(n-3)
            dp[n]=ans
            return ans
        return solve(n)
