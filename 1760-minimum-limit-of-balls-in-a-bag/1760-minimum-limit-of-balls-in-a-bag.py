import math
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left = 1 
        right = max(nums)

        while left < right: 
            mid = (left + right) // 2 
            if self.isPossible(mid, nums, maxOperations):
                right = mid 
            else:
                left = mid + 1 
        return left 

    def isPossible(self, maxBalls, nums, maxOperations):
        total_oper = 0 

        for num in nums:
            oper = math.ceil(num / maxBalls) - 1
            total_oper += oper 

            if total_oper > maxOperations:
                return False 
        return True