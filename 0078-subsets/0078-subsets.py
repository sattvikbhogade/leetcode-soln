class Solution:
    def print_subseq(self, i, v, nums, n, ans):
        if i >= n:
            ans.append(v[:]) 
            return

        # Pick
        v.append(nums[i])
        self.print_subseq(i + 1, v, nums, n, ans)

        # Not pick
        v.pop()
        self.print_subseq(i + 1, v, nums, n, ans)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.print_subseq(0, [], nums, len(nums), ans)
        return ans
        