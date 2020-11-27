class Solution:
    def singleNumber(self, nums):
        unique = list(set(nums))
        double = unique + unique
        for i in nums:
            double.remove(i)
        return int(double[0])