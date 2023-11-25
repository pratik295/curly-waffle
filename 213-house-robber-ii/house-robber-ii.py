from typing import List

class Solution:
    def rob(self, houses: List[int]) -> int:
        def solve(start, end, memo):
            if start > end:
                return 0
            if start == end:
                return houses[start]

            if (start, end) in memo:
                return memo[(start, end)]

            rob_current = houses[start] + solve(start + 2, end, memo)
            skip_current = solve(start + 1, end, memo)

            result = max(rob_current, skip_current)
            memo[(start, end)] = result

            return result

        if not houses:
            return 0
        if len(houses) == 1:
            return houses[0]

        memo = {}
        case1 = solve(0, len(houses) - 2, memo)
        memo = {}
        case2 = solve(1, len(houses) - 1, memo)

        return max(case1, case2)

