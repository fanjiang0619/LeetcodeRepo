class Solution:
    def reverse(self, x: int) -> int:
        indicator = 1
        if x < 0:
            indicator = -1
            x *= -1
        output = 0
        x = list(str(x))
        length = len(x)
        for i in range(length):
            output += int(x.pop()) * 10**(length - i - 1)
        if not (output >= -2**31 and output <= 2**31 - 1):
            return 0
        return output * indicator