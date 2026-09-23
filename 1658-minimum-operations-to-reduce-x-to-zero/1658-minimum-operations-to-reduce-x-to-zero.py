class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        totalSum = sum(nums)
        target = totalSum - x

        left = 0
        windowSum = 0
        maxLength = -1

        for right in range(len(nums)):
            windowSum += nums[right]

            while left <= right and windowSum > target:
                windowSum -= nums[left]
                left += 1

            if windowSum == target:
                maxLength = max(maxLength, right - left + 1)

        if maxLength == -1:
            return -1

        return len(nums) - maxLength