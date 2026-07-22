class Solution:
    def helper(self, i, v, total, candidates, n, target, ans):
        if total == target:
            ans.append(v[:])
            return

        if total > target:
            return

        if i == n:
            return

        # Tatargete
        v.append(candidates[i])
        self.helper(i, v, total + candidates[i], candidates, n, target, ans)
        

        # Not tatargete
        v.pop()
        self.helper(i + 1, v, total, candidates, n, target, ans)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        v = []
        self.helper(0, v, 0, candidates, n, target, ans)
        return ans