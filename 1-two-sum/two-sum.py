class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff not in counter:
                counter[nums[i]]=i
            else:
                return (counter[diff],i)
