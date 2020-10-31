class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        else:
            pointer1 = 0
            for i in range(len(nums)-1):
                pointer2 = i+1
                if nums[pointer1] != nums[pointer2]:
                    pointer1 += 1
                    nums[pointer1] = nums[pointer2]
                else:
                    pointer2 += 1
            return pointer1 + 1 