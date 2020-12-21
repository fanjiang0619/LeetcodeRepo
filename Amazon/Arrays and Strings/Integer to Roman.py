class Solution:
    def intToRoman(self, num: int) -> str:
        rule = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
        key = list(rule.keys())
        result = []
        while num != 0:
            char = key.pop()
            result.append(rule[char] * (num//char))
            num %= char
        return "".join(result)