class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        rule = {")": "(", "]": "[", "}": "{"}
        right = []
        for i in s:
            if i in rule.values():
                right.append(i)
            else: 
                if right == [] or rule[i] != right.pop():
                    return False
        return right == []

class Solution:
    def isValid(self, s: str) -> bool:
        while len(s) > 0:
            l = len(s)
            s = s.replace('()','').replace('{}','').replace('[]','')
            if l==len(s): return False
        return True