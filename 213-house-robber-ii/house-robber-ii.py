from typing import List

class Solution:
    def rob(self, houses: List[int]) -> int:
        def rob_linear(nums):
            dp = [-1] * len(nums)
            return rob_recursive(len(nums) - 1, nums, dp)

        def rob_recursive(i, nums, dp):
            if i < 0:
                return 0
            if dp[i] != -1:
                return dp[i]

            rob_current = nums[i] + rob_recursive(i - 2, nums, dp)
            skip_current = rob_recursive(i - 1, nums, dp)
            dp[i] = max(rob_current, skip_current)
            return dp[i]

        if not houses:
            return 0
        if len(houses) == 1:
            return houses[0]
        if len(houses) == 2:
            return max(houses[0], houses[1])

        # Case 1: Include the first house, exclude the last one
        case1 = rob_linear(houses[:-1])

        # Case 2: Exclude the first house, include the last one
        case2 = rob_linear(houses[1:])

        # Take the maximum of the two cases
        return max(case1, case2)

