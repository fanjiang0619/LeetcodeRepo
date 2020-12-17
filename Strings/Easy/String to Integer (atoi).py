class Solution:
    # @return an integer
    def myAtoi(self, str):
        str = str.strip()
        str = re.findall('^[\+\-0]*\d+', str)

        try:
            result = int(''.join(str))
            if result < -2**31:
                return -2**31
            elif result > 2**31 - 1:
                return 2**31 - 1
            else:
                return result
        except:
            return 0

class Solution:
    # @return an integer
    def myAtoi(self, s):
        s = s.strip()
        if s == "":
            return 0
        sign = 1
        if s[0] == "+":
            s = s[1:]
        elif s[0] == "-":
            sign = -1
            s = s[1:]
        str_num = [str(i) for i in range(10)]
        if s != "" and s[0] in str_num:
            i = 0
            result = []
            while i < len(s) and s[i] in str_num:
                result.append(s[i])
                i += 1
            result = sign * int("".join(result))
            if result < -2**31:
                return -2**31
            elif result > 2**31 - 1:
                return 2**31 - 1
            else:
                return result
        else:
            return 0