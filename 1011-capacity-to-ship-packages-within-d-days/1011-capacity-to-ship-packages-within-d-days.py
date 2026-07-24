class Solution:
    def isPossible(self, weights, c, days):
        daysNeeded = 1 
        curr = 0 
        
        for i in range(len(weights)):
            curr += weights[i]
            if curr > c:
                daysNeeded += 1 
                curr = weights[i]
        return daysNeeded <= days
        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total_weight = 0 
        max_weight = 0 
        
        for i in range(len(weights)):
            total_weight += weights[i]
            max_weight = max(max_weight, weights[i])
            
        l = max_weight
        r = total_weight 
        
        while(l<r):
            mid = (l+r)//2 
            if self.isPossible(weights, mid, days):
                r = mid 
            else:
                l = mid + 1 
        return l
        