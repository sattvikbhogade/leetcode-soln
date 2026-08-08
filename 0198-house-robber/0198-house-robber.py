class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n

        def helper(i):
            if i == 0:
                return nums[0]

            if i == 1:
                return max(nums[0], nums[1])

            if dp[i] != -1:
                return dp[i]

            skip = helper(i - 1)
            take = nums[i] + helper(i - 2)

            dp[i] = max(skip, take)

            return dp[i]

        return helper(n - 1)