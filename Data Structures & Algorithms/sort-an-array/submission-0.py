class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        while True:
            count = 0 
            for i in range(1, len(nums)):
                if nums[i]<nums[i-1]:
                    count+=1 
                    nums[i-1], nums[i] = nums[i], nums[i-1]
            if count==0 :
                break
        return nums
        