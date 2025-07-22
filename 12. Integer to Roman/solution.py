class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Convert an integer to a Roman numeral.
        Time complexity: O(1) since input range is fixed (1 to 3999).
        """
        val_to_roman = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'),  (90, 'XC'), (50, 'L'),  (40, 'XL'),
            (10, 'X'),   (9, 'IX'),  (5, 'V'),   (4, 'IV'),
            (1, 'I')
        ]
        
        result = ""
        for val ,roman in val_to_roman:
            while num >= val:
                result += roman
                num -= val
                
        return result
        
        
        

num = 3749

solu = Solution()
print(solu.intToRoman(num))

# print(str(num)[::-1])