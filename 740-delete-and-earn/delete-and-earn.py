from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp={}
        if not nums:
            return 0
        
        def rob(i, count):
            if i < 0:
                return 0
            if i in dp:
                return dp[i]
            
            # Choose to delete the current element
            delete_current = rob(i - 2, count) + count[i]
            
            # Choose to skip the current element
            skip_current = rob(i - 1, count)
            
            res= max(delete_current, skip_current)
            dp[i]=res
            return res
        
        max_num = max(nums)
        count = [0] * (max_num + 1)

        for num in nums:
            count[num] += num

        return rob(max_num, count)
