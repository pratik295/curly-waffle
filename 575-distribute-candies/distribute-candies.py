class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candies=set(candyType)
        rem=len(candies)
        total=len(candyType)//2
        if rem>=total:
            return total
        else:
            return rem