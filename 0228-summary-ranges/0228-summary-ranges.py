class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        result = []
        
        n = len(nums)
        
        if n == 0:
            return result 
            
        start = nums[0]
        
        for i in range(1, n+1):
            if i == n or nums[i] != nums[i-1] + 1:
                if start == nums[i-1]:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(nums[i-1]))
                
                if i < n:
                    start = nums[i]
        return result