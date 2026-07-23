class Solution:
    def helper(self, i, v, total, k, n, ans):
        # Valid combination
        if len(v) == k:
            if total == n:
                ans.append(v[:])
            return

        # Stop recursion
        if i > 9 or total > n:
            return

        # Pick
        v.append(i)
        self.helper(i + 1, v, total + i, k, n, ans)

        # Backtrack
        v.pop()

        # Not Pick
        self.helper(i + 1, v, total, k, n, ans)
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        v = []
        self.helper(1, v, 0, k, n, ans)
        return ans