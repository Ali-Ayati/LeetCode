### 3330. Find the Original Typed String I
*File:* `3330. Find the Original Typed String I/solution.py`  
**Description:** Given a string `word` that represents the result of Alice's typing, return the total number of possible original strings that Alice might have intended to type.

Alice may have accidentally held one key too long **at most once**, causing a character to appear multiple times. So we consider all valid original strings where at most one group of repeated characters may have one character fewer.

Example 1:  
Input: `word = "abbcccc"`  
Output: `5`  
Explanation: Possible original strings: `"abbcccc"`, `"abbccc"`, `"abbcc"`, `"abbc"`, `"abcccc"`.

Example 2:  
Input: `word = "abcd"`  
Output: `1`  
Explanation: Only possible original is `"abcd"`.

Example 3:  
Input: `word = "aaaa"`  
Output: `4`  
Explanation: You can remove 0 to 1 `'a'` from the group.

***Problem link***: https://leetcode.com/problems/find-the-original-typed-string-i

---

### 3330. Find the Original Typed String I  
*فایل:* `3330. Find the Original Typed String I/solution.py`  
**توضیح:** رشته‌ای به نام `word` داده شده که نتیجه نهایی تایپ آلیس روی صفحه‌کلید است. آلیس ممکن است تنها یک‌بار یکی از کلیدها را طولانی نگه داشته باشد و یک حرف چند بار تکرار شده باشد.

وظیفه شما این است که تعداد رشته‌های اولیه‌ی معتبری که آلیس ممکن بوده قصد تایپ آن‌ها را داشته باشد، پیدا کنید.

مثال ۱:  
ورودی: `word = "abbcccc"`  
خروجی: `5`  
توضیح: رشته‌های ممکن: `"abbcccc"`, `"abbccc"`, `"abbcc"`, `"abbc"`, `"abcccc"`

مثال ۲:  
ورودی: `word = "abcd"`  
خروجی: `1`  
توضیح: فقط `"abcd"` ممکن است.

مثال ۳:  
ورودی: `word = "aaaa"`  
خروجی: `4`  
توضیح: می‌توان ۰ تا ۱ بار یک `'a'` را حذف کرد.

***لینک مسعله***: https://leetcode.com/problems/find-the-original-typed-string-i
