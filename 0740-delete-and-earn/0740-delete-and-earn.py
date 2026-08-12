class Solution:
    def helper(self, i, points, dp):
        #Base case...
        if i == 0:
            return points[0]
        if i == 1:
            return max(points[0], points[1])
        if dp[i] != -1:
            return dp[i]

        pick = points[i] + self.helper(i-2, points, dp)
        notPick = 0 + self.helper(i - 1, points, dp)

        dp[i] = max(pick, notPick)

        return dp[i]

    def deleteAndEarn(self, nums: List[int]) -> int:
        maxValue = max(nums)

        points = [0] * (maxValue + 1)

        for num in nums:
            points[num] += num

        dp = [-1] * (maxValue + 1)

        return self.helper(maxValue, points, dp)
        