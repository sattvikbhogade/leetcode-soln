class Solution:

    def f(self, l, r, stoneValue):
        if l == r:
            return 0

        if self.dp[l][r] != -1:
            return self.dp[l][r]

        score = 0
        leftSum = 0
        rightSum = self.prefix[r + 1] - self.prefix[l]

        for i in range(l, r):

            leftSum += stoneValue[i]
            rightSum -= stoneValue[i]

            if leftSum < rightSum:

                if score >= 2 * leftSum:
                    continue

                score = max(
                    score,
                    leftSum + self.f(l, i, stoneValue)
                )

            elif leftSum > rightSum:

                if score >= 2 * rightSum:
                    break

                score = max(
                    score,
                    rightSum + self.f(i + 1, r, stoneValue)
                )

            else:

                score = max(
                    score,
                    leftSum + self.f(l, i, stoneValue),
                    rightSum + self.f(i + 1, r, stoneValue)
                )

        self.dp[l][r] = score

        return score


    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        # Prefix sum
        self.prefix = [0] * (n + 1)

        for i in range(n):
            self.prefix[i + 1] = self.prefix[i] + stoneValue[i]

        # DP table
        self.dp = [[-1] * n for _ in range(n)]

        return self.f(0, n - 1, stoneValue)