class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_nums=[]
        n=len(nums)
        for i in range(2*n):
            if i<n:
                new_nums.append(nums[i])
            else:
                new_nums.append(nums[i-n])
        return new_nums

            #at index 3 -> 0 1 2 3 
            #w e want to append 1
            
