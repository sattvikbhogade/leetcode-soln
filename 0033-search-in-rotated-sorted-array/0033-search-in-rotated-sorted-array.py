class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n-1 
        while (low <= high):
            mid = (low + high) // 2 
            if(nums[mid] == target):
                return mid
            elif(nums[mid] <= nums[high]):
                if(target >= nums[mid] and target <= nums[high]):
                    low = mid + 1 
                else:
                    high = mid - 1
            elif(nums[mid] >= nums[low]):
                if(target <= nums[mid] and target >= nums[low]):
                    high = mid - 1
                else:
                    low = mid + 1 
        return -1