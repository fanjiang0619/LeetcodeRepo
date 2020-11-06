class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        num = nums[:]
        num1 = num[-k:]
        del num[-k:]
        nums[:] = num1 + num
        print(nums)