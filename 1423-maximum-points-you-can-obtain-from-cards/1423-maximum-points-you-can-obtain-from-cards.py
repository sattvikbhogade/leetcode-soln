class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        currSum = 0 
        for i in range(k):
            currSum += cardPoints[i] 

        maxSum = currSum 

        left = k - 1 
        right = n - 1 

        while left >= 0:
            currSum -= cardPoints[left] 
            currSum += cardPoints[right]

            maxSum = max(maxSum, currSum)

            left -= 1 
            right -= 1
        return maxSum