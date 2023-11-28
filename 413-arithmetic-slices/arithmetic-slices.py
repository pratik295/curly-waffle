from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
    
        for i in range(n - 2):  # At least 3 elements needed for an arithmetic sequence
            diff = nums[i + 1] - nums[i]
            for j in range(i + 2, n):  # Subarray should have at least 3 elements
                if nums[j] - nums[j - 1] == diff:
                    count += 1
                else:
                    break  # If the difference is not maintained, break the inner loop
        
        return count

