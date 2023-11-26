from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp={}
        def solve(i, nums):
            if i == len(nums) - 1:
                return True
            
            if i in dp:
                return dp[i]

            jump = nums[i]
            while jump:
                next_position = i + jump
                if next_position < len(nums) and solve(next_position, nums):
                    dp[i]= True
                    return True
                jump -= 1

            dp[i]=False
            return False

        return solve(0, nums)
