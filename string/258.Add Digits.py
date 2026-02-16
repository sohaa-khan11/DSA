"""
258. Add Digits
link: https://leetcode.com/problems/add-digits/description/
"""
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if (num%9==0):
            return 9
        else:
            return num%9
            
