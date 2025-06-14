# LeetCode Practice Problems

This repository contains my solutions to selected problems from [LeetCode](https://leetcode.com/).  
Each problem is organized by its number and title.  

---

## Solved Problems

### 1. Two Sum
*File:* `1. Two Sum/solution.py`  
**Description:** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
<!-- Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1] -->

---

### 2. Add Two Numbers
*File:* `2. Add Two Numbers/solution.py`  
**Description:** You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
<!-- Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1] -->

---

### 3. Longest Substring Without Repeating Characters
*File:* `3. Longest Substring Without Repeating Characters/solution.py`  
**Description:** Given a string s, return the longest palindromic substring in s.
<!-- Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb" -->

---

### 5. Longest Palindromic Substring
*File:* `5. Longest Palindromic Substring/solution.py`  
**Description:** Given a string s, find the length of the longest substring without duplicate characters.
<!-- Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring. -->

---

### 9. Palindrome Number
*File:* `9. Palindrome Number/solution.py`  
**Description:** Given an integer x, return true if x is a palindrome, and false otherwise. 
<!-- Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome. -->

---

### 13. Roman to Integer
*File:* `13. Roman to Integer/solution.py`  
**Description:** Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
<!-- Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4. -->

---

### 14. Longest Common Prefix
*File:* `14. Longest Common Prefix/solution.py`  
**Description:** Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
<!-- Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings. -->

---

## How to Use

Each directory is named based on the LeetCode problem number and title.  
Inside each directory, you will typically find:
- Python solution(s)
- Possibly helper functions (e.g., for building linked lists)
- Optional: Test code or notes

---
---

# تمرین مسائل LeetCode

این مخزن شامل راه‌حل‌های منتخب من برای مسائل سایت [LeetCode](https://leetcode.com/) است.  
هر مسئله بر اساس شماره و عنوان آن سازماندهی شده است.  

---

## مسائل حل شده

### 1. Two Sum
*فایل:* `1. Two Sum/solution.py`  
**توضیح:** به شما آرایه‌ای از اعداد صحیح nums و یک عدد هدف target داده شده است. باید اندیس دو عدد را پیدا کنید که جمع آنها برابر با target شود.

فرض کنید هر ورودی دقیقاً یک جواب دارد و نمی‌توانید از یک عنصر دو بار استفاده کنید.  
می‌توانید پاسخ را به هر ترتیبی بازگردانید.  
<!-- Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1] -->

---

### 2. Add Two Numbers
*فایل:* `2. Add Two Numbers/solution.py`  
**توضیح:** دو لیست پیوندی غیرخالی دارید که اعداد غیرمنفی را نمایش می‌دهند. ارقام به صورت معکوس ذخیره شده‌اند. دو عدد را جمع کنید و حاصل را به صورت یک لیست پیوندی بازگردانید.
فرض کنید اعداد هیچ صفر پیشوندی به جز خود صفر ندارند.  
<!-- Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1] -->

---

### 3. Longest Substring Without Repeating Characters
*فایل:* `3. Longest Substring Without Repeating Characters/solution.py`  
**توضیح:** یک رشته s داده شده است. باید طول بلندترین زیررشته‌ای را بیابید که در آن هیچ کاراکتری تکراری وجود نداشته باشد.
<!-- Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb" -->

---

### 5. Longest Palindromic Substring
*File:* `5. Longest Palindromic Substring/solution.py`  
**Description:** یک رشته s داده شده است. هدف پیدا کردن بلندترین زیررشته‌ای است که از دو طرف یکسان (پالیندروم) باشد.
<!-- Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring. -->

---

### 9. Palindrome Number
*فایل:* `9. Palindrome Number/solution.py`  
**توضیح:** عدد صحیح x داده شده است. اگر عدد پالیندروم باشد (از چپ به راست و راست به چپ برابر باشد) مقدار True، در غیر این صورت False بازگردانید. 
<!-- Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome. -->

---

### 13. Roman to Integer
*فایل:* `13. Roman to Integer/solution.py`  
**توضیح:** شته‌ای شامل عدد رومی داده شده است. هدف، تبدیل آن به عدد صحیح معادل است.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
<!-- Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4. -->

---

### 14. Longest Common Prefix
*فایل:* `14. Longest Common Prefix/solution.py`  
**توضیح:** یک آرایه از رشته‌ها داده شده است. باید بلندترین پیشوند مشترک بین تمام رشته‌ها را بیابید.

اگر پیشوند مشترکی وجود نداشت، رشته‌ی خالی "" را برگردانید.
<!-- Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings. -->

---

## نحوه استفاده

هر دایرکتوری بر اساس شماره و عنوان مسئله LeetCode نامگذاری شده است.  
داخل هر دایرکتوری معمولاً موارد زیر پیدا می‌شود:  
- راه‌حل‌های پایتون  
- توابع کمکی (مانند ساختن لیست پیوندی)  
- اختیاری: کد تست یا یادداشت‌ها