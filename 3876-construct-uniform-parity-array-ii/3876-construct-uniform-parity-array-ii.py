class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        has_odd = False
        min_odd = float('inf')

        for x in nums1:
            if x % 2 == 1:
                has_odd = True
                min_odd = min(min_odd, x)

        # Already uniform: all even
        if not has_odd:
            return True

        # Need every even number to be >= smallest odd
        for x in nums1:
            if x % 2 == 0 and x < min_odd:
                return False

        return True