class Solution:
    def time_to_eat(self, piles, n, speed):
        total_time = 0
        for i in range(n):
            total_time += (piles[i] + speed - 1) // speed
        return total_time
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        low = 1
        high = max(piles)
        ans = -1
        
        while (low <= high):
            mid = low + (high - low) // 2 
            if self.time_to_eat(piles, n, mid) <= h:
                ans = mid 
                high = mid - 1 
            else:
                low = mid + 1 
        return ans 
    
    