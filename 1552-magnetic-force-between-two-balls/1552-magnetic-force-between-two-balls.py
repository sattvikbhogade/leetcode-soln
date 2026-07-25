class Solution:
    def canPlace(self, position, force, m):
        ballsPlaced = 1
        last = position[0]

        for i in range(1, len(position)):
            if position[i] - last >= force:
                ballsPlaced += 1
                last = position[i]

                if ballsPlaced == m:
                    return True

        return False
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        low = 1
        high = position[-1] - position[0]
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if self.canPlace(position, mid, m):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
        