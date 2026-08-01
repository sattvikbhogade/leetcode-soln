class Solution:
    def canCoverAllHouses(self, houses, heaters, radius):
        i = 0
        n = len(houses)

        for heater in heaters:

            while i < n and houses[i] < heater - radius:
                return False

            while i < n and houses[i] <= heater + radius:
                i += 1

            if i == n:
                return True

        return i == n
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        low = 0
        high = max(
            abs(houses[0] - heaters[-1]),
            abs(houses[-1] - heaters[0])
        )

        res = high

        while low <= high:
            guess = low + (high - low) // 2

            if self.canCoverAllHouses(houses, heaters, guess):
                res = guess
                high = guess - 1
            else:
                low = guess + 1

        return res