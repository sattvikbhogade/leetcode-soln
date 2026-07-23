class Solution:
    def helper(self, v, nums, visited, ans):
        if len(v) == len(nums):
            ans.append(v[:])
            return
        for i in range(len(nums)):
            if visited[i]:
                continue

            visited[i] = True 
            v.append(nums[i])

            self.helper(v, nums, visited, ans) 

            v.pop()
            visited[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        v = []
        ans = []
        visited = [False]*len(nums)
        self.helper(v, nums, visited, ans)
        return ans