class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def kadane(nums):
            maxsum=nums[0]
            cursum=0
            for n in nums:
                cursum=max(cursum,0)
                cursum+=n
                maxsum=max(maxsum,cursum)
            return maxsum
        return kadane(nums)
        
                
                
                
            
