import time


# String-based reversal
class Solution1:
    def reverse(self, x: int) -> int:
        """
        Reverse the digits of a 32-bit signed integer using string slicing.
        
        If the reversed integer overflows 32-bit signed integer range [-2^31, 2^31 - 1], return 0.

        Time Complexity: O(n), where n is the number of digits in x.
        This method uses string conversion and slicing, which are relatively slower due to overhead.

        Args:
            x (int): The integer to reverse.

        Returns:
            int: The reversed integer, or 0 if it overflows.
        """
        
        result = int("-" + str(abs(x))[::-1] if x < 0 else str(x)[::-1])
        if not -2**31 <= result <= 2**31 - 1:
            return 0

        return result
    


start = time.time()
x = -123
a = Solution1()
print(a.reverse(x))
end = time.time()
print("String-based reversal Execution time:", end - start, "seconds")

# --------------------------------------------------

# Math-based reversal
class Solution2:
    def reverse(self, x: int) -> int:
        """
        Reverse the digits of a 32-bit signed integer using mathematical operations.

        Handles sign separately and constructs the reversed number by extracting digits.

        Time Complexity: O(n), where n is the number of digits in x.
        This approach is faster and more memory-efficient than string-based methods.

        Args:
            x (int): The integer to reverse.

        Returns:
            int: The reversed integer, or 0 if it overflows.
        """
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        
        result = sign * rev
        
        if not -2**31 <= result <= 2**31 - 1:
            return 0
        
        return result
    
 
 
   
start = time.time()
x = -123
a = Solution2()
print(a.reverse(x))
end = time.time()
print("Math-based reversal Execution time:", end - start, "seconds")