class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        repeated = -1 
        missing =  -1 
        
        for i in range(n):
            index = abs(nums[i]) - 1 
            if nums[index] < 0:
                repeated = abs(nums[i])
            else:
                nums[index] = -nums[index]
        
        for i in range(n):
            if nums[i] > 0:
                missing = i+1 
                break 
            
        return [repeated, missing]