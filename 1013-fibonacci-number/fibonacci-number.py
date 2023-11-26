class Solution:
    def fib(self, n: int) -> int:
        dp={}
        def solve(n):

            if n<=1:
                return n
            if n in dp:
                return dp[n]
            res= solve(n-1)+solve(n-2)
            dp[n]=res
            return res
        return solve(n)