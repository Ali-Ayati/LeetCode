class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        result = 0
        sign = 1

        # Step 1: skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: check sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Step 3: convert digits to number
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        # Step 4: clamp to 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result
    
    

s = " 2021 - 22"

solu = Solution()

print(solu.myAtoi(s))