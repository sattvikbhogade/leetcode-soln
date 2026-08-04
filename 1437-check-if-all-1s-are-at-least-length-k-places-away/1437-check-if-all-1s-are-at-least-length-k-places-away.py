class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        lastOne = -1

        for i in range(len(nums)):
            if nums[i] == 1:

                if lastOne != -1:
                    distance = i - lastOne - 1

                    if distance < k:
                        return False

                lastOne = i

        return True
