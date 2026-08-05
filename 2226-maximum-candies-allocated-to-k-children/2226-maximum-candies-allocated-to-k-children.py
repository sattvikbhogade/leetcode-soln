class Solution:
    def canAllocateCandies(self, candies, k, numOfCandies):
        maxNumOfChildern = 0 

        for pile in candies:
            maxNumOfChildern += pile // numOfCandies 
        
        return maxNumOfChildern >= k

    def maximumCandies(self, candies: List[int], k: int) -> int:
        maxCandies = 0 
        for candy in candies:
            maxCandies = max(maxCandies, candy)
        
        left = 0 
        right = maxCandies 

        while left < right:
            mid = (left + right + 1) // 2 

            if self.canAllocateCandies(candies, k, mid):
                left = mid 
            else:
                right = mid - 1 
        return left