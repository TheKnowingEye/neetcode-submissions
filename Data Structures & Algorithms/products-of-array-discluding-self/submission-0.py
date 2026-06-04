class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix_mul = [0]*length
        
        for i in range(length):
            if i == 0: 
                prefix_mul[i] = nums[i]
                continue
            prefix_mul[i]=prefix_mul[i-1]*nums[i]
        
        suffix_mul = [0]*length
        for i in range(length-1,0,-1):
            if i==length-1:
                suffix_mul[i] = nums[i]
                continue
            suffix_mul[i] = suffix_mul[i+1]*nums[i]
        
        ans = [0]*length
        for  i in range(length):
            if i == 0 :
                ans[i]=suffix_mul[i+1]
                
            elif i == length-1 :
                ans[i]=prefix_mul[i-1]
                
            else:
                ans[i]=prefix_mul[i-1]*suffix_mul[i+1]
        return ans