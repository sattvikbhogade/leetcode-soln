class Solution:
    def countSubarrays(self, nums, maxSum):
        subarrays = 1
        currentSum = 0

        for num in nums:
            if currentSum + num <= maxSum:
                currentSum += num
            else:
                subarrays += 1
                currentSum = num

        return subarrays
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums) 
        
        while low <= high:
            mid = low + (high - low)//2 
            requiredSubarrays = self.countSubarrays(nums, mid)

            if requiredSubarrays > k:
                low = mid + 1 
            else:
                ans = mid 
                high = mid - 1 
        return ans
        