class Solution:
    #Tabulation - Bottom Up
    

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n 
        dp[0] = nums[0]
        if n == 1:
            return nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            pick = nums[i] + dp[i - 2]
            not_pick = dp[i - 1]
            dp[i] = max(pick, not_pick)
        return dp[n - 1]
#T.C.= O(n)
#S.C.= O(n)