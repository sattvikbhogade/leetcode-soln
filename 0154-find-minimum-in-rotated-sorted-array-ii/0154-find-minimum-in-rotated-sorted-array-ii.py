class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low  = 0
        high = n - 1
        
        ans = float("inf")
        while low <= high:
            mid = (low + high) // 2

            # all are equal
            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                ans = min(ans, nums[mid])
                low = low + 1
                high = high - 1

            #left sorted
            elif nums[low] <= nums[mid]:
                ans = min(ans, nums[low])
                low = mid + 1
            
            #right sorted
            else:
                ans = min(ans, nums[mid])
                high = mid - 1
        return ans