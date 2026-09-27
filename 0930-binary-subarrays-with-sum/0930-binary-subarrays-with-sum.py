class Solution:

    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def countAtMost(k):
            if k < 0:
                return 0

            left = 0
            total = 0
            ans = 0

            for right in range(len(nums)):
                total += nums[right]

                while total > k:
                    total -= nums[left]
                    left += 1

                ans += right - left + 1

            return ans

        return countAtMost(goal) - countAtMost(goal - 1)