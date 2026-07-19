class Solution:
    def numOfBouquets(self, bloomDay, n, k, d):
        count = 0 
        bouquet = 0 
        for i in range(n):
            if bloomDay[i] <= d:
                count += 1 
                if count == k:
                    bouquet += 1 
                    count = 0 
            else:
                count = 0 
        return bouquet

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay) 
        if (n < m*k):
            return -1 
        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1 
        
        while low <= high:
            mid = low + (high - low) // 2 
            if self.numOfBouquets(bloomDay, n, k, mid) >= m: 
                ans = mid 
                high = mid - 1 
            else:
                low = mid + 1 
        return ans