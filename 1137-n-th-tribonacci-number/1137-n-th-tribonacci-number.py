class Solution:
    def helper(self, n, dp):
        if n == 0:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 1

        if dp[n] != -1:
            return dp[n]

        dp[n] = (
            self.helper(n - 1, dp)
            + self.helper(n - 2, dp)
            + self.helper(n - 3, dp)
        )

        return dp[n]
        dp[n] = self.helper(n-1, dp)+self.helper(n-2, dp)+self.helper(n-3, dp)
        return dp[n]
    def tribonacci(self, n: int) -> int:
        dp = [-1] * (n + 1)
        return self.helper(n, dp)