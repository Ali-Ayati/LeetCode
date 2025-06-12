# LeetCode Practice Problems

This repository contains my solutions to selected problems from [LeetCode](https://leetcode.com/).  
Each problem is organized by its number and title.  

---

## Solved Problems

### 1. Two Sum
*File:* `1. Two Sum/solution.py`  
*Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.*  
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
*Description: You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.*  
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

### 9. Palindrome Number
*File:* `9. Palindrome Number/solution.py`  
*Description: Given an integer x, return true if x is a palindrome, and false otherwise.*  
<!--Example 1:
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
*توضیح: به شما آرایه‌ای از اعداد صحیح nums و یک عدد هدف target داده شده است. باید اندیس دو عدد را پیدا کنید که جمع آنها برابر با target شود.*

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
*توضیح: دو لیست پیوندی غیرخالی دارید که اعداد غیرمنفی را نمایش می‌دهند. ارقام به صورت معکوس ذخیره شده‌اند. دو عدد را جمع کنید و حاصل را به صورت یک لیست پیوندی بازگردانید.*

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

### 9. Palindrome Number
*فایل:* `9. Palindrome Number/solution.py`  
*توضیح: عدد صحیح x داده شده است. اگر عدد پالیندروم باشد (از چپ به راست و راست به چپ برابر باشد) مقدار True، در غیر این صورت False بازگردانید.*  
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

## نحوه استفاده

هر دایرکتوری بر اساس شماره و عنوان مسئله LeetCode نامگذاری شده است.  
داخل هر دایرکتوری معمولاً موارد زیر پیدا می‌شود:  
- راه‌حل‌های پایتون  
- توابع کمکی (مانند ساختن لیست پیوندی)  
- اختیاری: کد تست یا یادداشت‌ها