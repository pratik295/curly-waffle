class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp={}
        def solve(i,cost):
            if i>=len(cost):
                return 0 
            if i in dp:
                return dp[i]
            
            a=cost[i]+solve(i+1,cost)
            b=cost[i]+solve(i+2,cost)
            res=min(a,b)
            dp[i]=res
            return res
        return min(solve(0,cost),solve(1,cost))