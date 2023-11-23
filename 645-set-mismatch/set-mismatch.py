class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        real_sum=n*(n+1)//2
        actual_sum=sum(set(nums))

        dup=sum(nums)-actual_sum 
        missing=real_sum-actual_sum
        return[dup,missing]