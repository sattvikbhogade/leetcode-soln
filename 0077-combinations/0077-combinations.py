class Solution:
    def helper(self, i, v, k, n, ans):
        if (len(v) == k):
            ans.append(v[:])
            return
        if (i>n):
            return

        v.append(i)
        self.helper(i+1, v, k, n, ans)
        v.pop()
        self.helper(i+1, v, k, n, ans)

    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        v = []
        self.helper(1, v, k, n, ans)
        return ans