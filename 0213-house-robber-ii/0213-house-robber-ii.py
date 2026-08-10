class Solution:
    #Tabulation - Bottom_Up
    def helperFunction(self, nums, start, end):
        length = end - start + 1
        if length == 1:
            return nums[start]
        dp = [0] * length
        dp[0] = nums[start]
        dp[1] = max(nums[start], nums[start + 1])
        for i in range(2, length):
            pick = nums[start + i] + dp[i - 2]
            skip = dp[i - 1]
            dp[i] = max(pick, skip)
        return dp[length - 1]


    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.helperFunction(nums, 0, n - 2), self.helperFunction(nums, 1, n - 1))
        