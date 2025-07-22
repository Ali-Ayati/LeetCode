### 12. Integer to Roman
*File:* `12. Integer to Roman/solution.py`  
**Description:** Given an integer, convert it to a Roman numeral.

Roman numerals use the following symbols:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Conversion rules:
- Use the largest possible Roman symbol at each step, subtract its value, and continue.
- Use subtractive notation for values starting with 4 or 9, e.g., 4 → IV, 9 → IX, 40 → XL.
- Powers of 10 (I, X, C, M) can be repeated up to 3 times. Symbols like V, L, D cannot be repeated.

Example 1:  
Input: `num = 3749`  
Output: `"MMMDCCXLIX"`

Example 2:  
Input: `num = 58`  
Output: `"LVIII"`

Example 3:  
Input: `num = 1994`  
Output: `"MCMXCIV"`

***Problem link***: https://leetcode.com/problems/integer-to-roman

---

### 12. Integer to Roman  
*فایل:* `12. Integer to Roman/solution.py`  
**توضیح:** عددی صحیح داده شده است، آن را به عدد رومی (Roman Numeral) تبدیل کنید.

اعداد رومی با استفاده از نمادهای زیر ساخته می‌شوند:

| نماد | مقدار |
|------|--------|
| I    | 1      |
| V    | 5      |
| X    | 10     |
| L    | 50     |
| C    | 100    |
| D    | 500    |
| M    | 1000   |

قوانین تبدیل:
- در هر مرحله، بزرگ‌ترین نماد ممکن انتخاب و از عدد کم می‌شود.
- اگر عدد با ۴ یا ۹ شروع شود، از روش کاهشی استفاده می‌شود. مثلاً 4 → IV و 9 → IX.
- تنها توان‌های ۱۰ (I, X, C, M) می‌توانند حداکثر ۳ بار پشت سر هم تکرار شوند.

مثال ۱:  
ورودی: `num = 3749`  
خروجی: `"MMMDCCXLIX"`

مثال ۲:  
ورودی: `num = 58`  
خروجی: `"LVIII"`

مثال ۳:  
ورودی: `num = 1994`  
خروجی: `"MCMXCIV"`

***لینک مسعله***: https://leetcode.com/problems/integer-to-roman