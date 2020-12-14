class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[\W_]+', '', s).lower()
        for i in range(len(s)//2):
            if s[i] != s[-i-1]:
                return False
        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[\W_]+', '', s).lower()
        if s != s[::-1]:
            return False
        return True
    
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[\W_]+', '', s).lower()
        return s == s[::-1]