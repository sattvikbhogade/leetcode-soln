class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = 0
        answer = 0

        for i in range(len(nums)):
            if frequency == 0:
                answer = nums[i]
            if(answer == nums[i]):
                frequency += 1
            else:
                frequency -= 1
        return answer