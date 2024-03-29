class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        rotated = sorted(nums)
        for i in range(n):
            if nums[i:]+nums[:i] == rotated:
                return True
        return False