# Problem: Palindrome Number
# LeetCode: https://leetcode.com/problems/palindrome-number/
# Problem Number: 9
# Difficulty: Easy
# Language: Python

class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        t = x
        reversed_number = 0

        while x > 0:
            digit = x % 10
            reversed_number = reversed_number * 10 + digit
            x = x // 10

        return t == reversed_number
