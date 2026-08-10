class Solution:
    #Memoization - Top to Down
    def helper(self, i, nums, dp):
        #Base case...
        if i == 0:
            return nums[0]
        if i == 1:
            return max(nums[0], nums[1])
        if dp[i] != -1:
            return dp[i]

        pick = nums[i] + self.helper(i-2, nums, dp)
        notPick = 0 + self.helper(i - 1, nums, dp)

        dp[i] = max(pick, notPick)

        return dp[i]

    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)

        return self.helper(len(nums) - 1, nums, dp)