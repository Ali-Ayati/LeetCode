class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]  # substring is between left+1 and right-1
        
        longest = ""
        for i in range(len(s)):
            # Odd length
            temp1 = expand_around_center(i, i)
            # Even length
            temp2 = expand_around_center(i, i+1)

            # Choose the longer one
            if len(temp1) > len(longest):
                longest = temp1
            if len(temp2) > len(longest):
                longest = temp2

        return longest
            
    
s = "babad"
a = Solution()
print(a.longestPalindrome(s=s))

# print(len(s))