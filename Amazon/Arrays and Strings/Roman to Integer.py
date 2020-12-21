class Solution:
    def romanToInt(self, s: str) -> int:
        rule = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M": 1000}
        minus_rule = {"I":["V", "X"], "X":["L", "C"], "C":["D", "M"]}
        result = 0
        last = len(s) - 1
        sign = 1
        for i, c in enumerate(s):
            if c in minus_rule and i != last:
                if s[i+1] in minus_rule[c]:
                    sign = -1
            result += sign * rule[c]
            sign = 1
        return result

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M": 1000}
        total = 0
        i = 0
        while i < len(s):
            # If this is the subtractive case.
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total += values[s[i + 1]] - values[s[i]]
                i += 2
            # Else this is NOT the subtractive case.
            else:
                total += values[s[i]]
                i += 1
        return total

class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number