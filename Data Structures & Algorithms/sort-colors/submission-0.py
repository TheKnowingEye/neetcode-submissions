class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        low, mid = 0, 0 
        high = length-1 
        
        while mid<=high:
            if nums[mid] == 0 :
                nums[low], nums[mid] = nums[mid], nums[low]
                low+=1 
            if nums[mid] == 2 :
                nums[high], nums [mid] = nums[mid], nums[high]
                high-=1
            else :
                mid+=1 
        return nums