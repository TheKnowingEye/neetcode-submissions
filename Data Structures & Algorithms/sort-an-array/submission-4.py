class Solution:
    def sortTwoSortedArrays(self,arr1: List[int], arr2: List[int]) -> List[int]:
        l, r = 0, 0 
        _sorted = [0]*(len(arr1) + len(arr2))
        i = 0
        while l<len(arr1) and r<len(arr2):
            if arr1[l] < arr2[r]: 
                _sorted[i] = arr1[l]
                l+=1
            else :
                _sorted[i] = arr2[r]
                r+=1
            i+=1     
        while l<len(arr1):
            _sorted[i] = arr1[l]
            i+=1 
            l+=1 
        while r<len(arr2):
            _sorted[i] = arr2[r]
            i+=1 
            r+=1 
        return _sorted

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1 :
            return nums
        m = n // 2 
        L = nums[:m]
        R = nums[m:]
        L = self.sortArray(L)
        R = self.sortArray(R)
        sorted_array=self.sortTwoSortedArrays(L,R) 

        return sorted_array