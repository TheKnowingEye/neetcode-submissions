class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i, 0 , -1):
                if nums[j-1]>nums[j]:
                    nums[j-1], nums[j] = nums[j], nums[j-1]
                else:
                    break
        return nums
        