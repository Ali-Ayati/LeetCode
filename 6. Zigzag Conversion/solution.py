from collections import defaultdict

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Converts a string into a zigzag pattern on a given number of rows and reads it line by line.

        Args:
            s (str): The input string to convert.
            numRows (int): The number of rows for the zigzag pattern.

        Returns:
            str: The zigzag-converted string read row by row.

        Time Complexity: O(n), where n is the length of the string.
        Slightly slower due to use of defaultdict and repeated string key construction.
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        row = 0
        my_dict = defaultdict(list)
        flag = True

        for i in range(len(s)):
            if row == 0 or row == numRows - 1:
                flag = not flag
                
            my_dict[f"row{row}"].append(s[i])
            row += 1 if flag else -1
                                
        result = ""
        for i in range(numRows):
            result += "".join(my_dict[f"row{i}"])
            
        return result


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Converts a string into a zigzag pattern on a given number of rows and reads it line by line.

        Args:
            s (str): The input string to convert.
            numRows (int): The number of rows for the zigzag pattern.

        Returns:
            str: The zigzag-converted string read row by row.

        Time Complexity: O(n), where n is the length of the string.
        Faster due to use of direct index-based list and efficient string join.
        Runtime: 9ms
        Beats: 72.49%
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = ['' for _ in range(numRows)]
        row = 0
        flag = False

        for char in s:
            rows[row] += char
            if row == 0 or row == numRows - 1:
                flag = not flag
            row += 1 if flag else -1

        return ''.join(rows)
    
    
s = "PAYPALISHIRING"
numRows = 3

"""
P   A   H   N
A P L S I I G
Y   I   R
"""

a = Solution()
print(a.convert(s=s, numRows=numRows))