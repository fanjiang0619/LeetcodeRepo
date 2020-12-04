class Solution:
    
    # collections.Counter(nums1)
    # for num in nums1:
    #       counts[num] = counts.get(num, 0) + 1
    
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = self.getDict(nums1)
        dict2 = self.getDict(nums2)
        result = []
        short, long = self.short(dict1, dict2)
        for j in short.keys():
            if j in long.keys():
                result.extend([j] * min(long[j], short[j]))
        return result
    
    def short(self, dict1, dict2):
        if len(dict1.keys()) < len(dict2.keys()):
            return dict1, dict2
        else:
            return dict2, dict1
        
    def getDict(self, num):
        d = {}
        for i in num:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        return d