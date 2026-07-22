class Solution:
    def helper(self, i, v, total, candidates, n, target, ans):
        if total == target:
            ans.append(v[:])
            return 
        if total > target:
            return 
        if i == n:
            return
        
        


        # Take
        v.append(candidates[i])
        self.helper(i + 1, v, total + candidates[i], candidates, n, target, ans)

        # Backtrack
        v.pop()

        while i + 1 < n and candidates[i]==candidates[i+1]:
            i+=1
        # Not Take
        self.helper(i + 1, v, total, candidates, n, target, ans)

        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.helper(0, [], 0, candidates, len(candidates), target, ans)
        return ans