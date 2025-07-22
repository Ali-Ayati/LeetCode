### 8. String to Integer (atoi)
*File:* `8. String to Integer (atoi)/solution.py`  
**Description:** Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer.

The algorithm follows these steps:

1. **Whitespace:** Ignore any leading whitespace.
2. **Signedness:** Check if the next character is '+' or '-', default to positive if absent.
3. **Conversion:** Read digits until a non-digit or the end of the string is reached.
4. **Clamping:** If the result is out of the 32-bit signed integer range, clamp it to \[-2³¹, 2³¹−1\].

Example 1:  
Input: s = "42"  
Output: 42

Example 2:  
Input: s = "   -042"  
Output: -42

Example 3:  
Input: s = "1337c0d3"  
Output: 1337

Example 4:  
Input: s = "0-1"  
Output: 0

Example 5:  
Input: s = "words and 987"  
Output: 0

***Problem link***: https://leetcode.com/problems/string-to-integer-atoi

---

### 8. String to Integer (atoi)  
*فایل:* `8. String to Integer (atoi)/solution.py`  
**توضیح:** تابع `myAtoi(string s)` باید یک رشته را به عدد صحیح ۳۲-بیتی علامت‌دار تبدیل کند.

مراحل عملکرد الگوریتم به صورت زیر است:

1. **فاصله:** فاصله‌های ابتدایی رشته نادیده گرفته می‌شوند.  
2. **علامت:** اگر اولین کاراکتر بعد از فاصله‌ها `+` یا `-` باشد، علامت عدد مشخص می‌شود. در غیر این صورت، عدد مثبت در نظر گرفته می‌شود.  
3. **تبدیل:** تا زمانی که کاراکترها عددی هستند، خواندن ادامه می‌یابد.  
4. **محدوده:** اگر عدد از محدوده‌ی مجاز \[-2³¹, 2³¹−1\] خارج شود، باید به نزدیک‌ترین عدد در این بازه گرد شود.

مثال ۱:  
ورودی: `"42"`  
خروجی: `42`

مثال ۲:  
ورودی: `"   -042"`  
خروجی: `-42`

مثال ۳:  
ورودی: `"1337c0d3"`  
خروجی: `1337`

مثال ۴:  
ورودی: `"0-1"`  
خروجی: `0`

مثال ۵:  
ورودی: `"words and 987"`  
خروجی: `0`

***لینک مسعله***: https://leetcode.com/problems/string-to-integer-atoi
