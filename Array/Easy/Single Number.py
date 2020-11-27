class Solution:
    def singleNumber1(self, nums):
        unique = list(set(nums))
        double = unique + unique
        for i in nums:
            double.remove(i)
        return int(double[0])

    def singleNumber2(self, nums):
        result = 2 * sum(set(nums)) - sum(nums)
        return result

    def singleNumber3(self, nums):
        a = 0
        for i in nums:
            a ^= i
        return a