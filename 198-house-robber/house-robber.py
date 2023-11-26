class Solution:
    def rob(self, nums: List[int]) -> int:
        dp={}
        
        def solve(i,nums):
            if i>=len(nums):
                return 0
            if i in dp:
                return dp[i]
            
            costa=nums[i]+solve(i+2,nums)
            costb=solve(i+1,nums)
            res= max(costa,costb)
            dp[i]=res 
            return res
        return solve(0,nums)