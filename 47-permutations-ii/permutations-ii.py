from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        # Base case: if there's only one element, return a list containing that element
        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permuteUnique(nums)
            for perm in perms:
                perm.append(n)
                res.append(perm)
            nums.append(n)

        new_set = set()
        unique_ans = []  # Use a different variable name to avoid confusion
        for perm in res:
            tup_perm = tuple(perm)
            if tup_perm not in new_set:
                unique_ans.append(list(tup_perm))
                new_set.add(tup_perm)
        return unique_ans
