class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        for i,num in enumerate(nums):
            rem = target - num
            if rem in seen:
                ans = [i, nums.index(rem)]
                return sorted(ans)
            seen.add(num)
        