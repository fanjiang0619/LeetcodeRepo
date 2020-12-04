class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 in nums: 
            idx = 0
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[idx], nums[i] = nums[i], nums[idx]
                    idx += 1
        return nums