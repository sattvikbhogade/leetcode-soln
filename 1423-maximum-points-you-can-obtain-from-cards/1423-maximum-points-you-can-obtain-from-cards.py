class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        totalSum = sum(cardPoints)
        
        if k == n:
            return totalSum

        windowLength = n - k
        windowSum = 0
        minSum = totalSum

        for i in range(n):
            windowSum += cardPoints[i]
            if i >= windowLength:
                windowSum -= cardPoints[i - windowLength]
            if i >= windowLength - 1:
                minSum = min(minSum, windowSum)

        return totalSum - minSum