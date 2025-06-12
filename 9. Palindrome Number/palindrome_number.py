
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Check if an integer is a palindrome using string reversal.

        This method converts the integer to a string, reverses it,
        then converts it back to an integer to compare with the original.

        Time complexity: O(n), where n is the number of digits in x.
        Memory usage is higher due to string allocation and conversion.

        This method is easy to implement and often fast for small inputs.
        However, the overhead of type conversions (int <-> str) can cause
        inconsistent performance on large inputs or in high-volume environments.
        """
        if x < 0:
            return False
        else:
            return int(str(x)[::-1]) == x


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Check if an integer is a palindrome using pure arithmetic.

        This method reverses the digits of the number mathematically,
        without converting it to a string. It avoids extra memory allocation
        and is usually more efficient for large numbers.

        Time complexity: O(n), where n is the number of digits in x.
        It generally performs faster in practice because it uses only
        arithmetic operations which are low-level and highly optimized.

        Arithmetic-based reversal is more performant especially on large numbers
        because it avoids string manipulation and type conversion overhead.
        """
        if x < 0:
            return False

        original = x
        reversed_num = 0

        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        return original == reversed_num


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        One-liner version of string-based palindrome check.

        While concise and clean, it may be slower than the arithmetic method
        due to implicit type conversions and string operations.

        Note: This version is functionally identical to the first one,
        just written in a single line using a ternary expression.

        In practice, this method can surprisingly be slower than expected,
        even though it looks compact — especially under Python interpreters
        or online judge systems like LeetCode where internal performance
        profiling and memory allocations affect runtime.
        """
        return False if x < 0 else int(str(x)[::-1]) == x
a = Solution()
print(a.isPalindrome(123))