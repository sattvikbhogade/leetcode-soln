import math

class Solution:
    def sum_division(self, nums, n, divisor):
        total_sum = 0
        for i in range(n):
            total_sum += math.ceil(nums[i] / divisor)
        return total_sum

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        low, high = 1, max(nums)
        ans = -1 
        while low <= high:
            mid = (low + high) // 2 
            if self.sum_division(nums, n, mid) <= threshold:
                ans = mid 
                high = mid - 1 
            else:
                low = mid + 1 
        return ans
        
    