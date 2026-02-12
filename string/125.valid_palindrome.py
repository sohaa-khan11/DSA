"""
125. Valid Palindrome
link: https://leetcode.com/problems/valid-palindrome/description/
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean=[]
        for i in s:
            if i.isalnum():
                clean.append(i.lower())
        str="".join(clean)
        if str==str[::-1]:
            return True
        else:
            return False