class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        current = 9
        start = 9
        ans = 10

        while n > 1:
            current *= start
            ans += current
            start -= 1
            n -= 1

        return ans
