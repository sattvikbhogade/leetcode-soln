class Solution:
    def f(self, ind, buy, prices, dp):

        # Base case
        if ind >= len(prices):
            return 0

        # Already calculated
        if dp[ind][buy] != -1:
            return dp[ind][buy]

        if buy == 1:
            # Buy today
            buy_stock = -prices[ind] + self.f(
                ind + 1, 0, prices, dp
            )

            # Don't buy today
            not_buy = self.f(
                ind + 1, 1, prices, dp
            )

            dp[ind][buy] = max(buy_stock, not_buy)

        else:
            # Sell today
            sell = prices[ind] + self.f(
                ind + 2, 1, prices, dp
            )

            # Don't sell today
            not_sell = self.f(
                ind + 1, 0, prices, dp
            )

            dp[ind][buy] = max(sell, not_sell)

        return dp[ind][buy]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1] * 2 for i in range(n)]      

        return self.f(0, 1, prices, dp)