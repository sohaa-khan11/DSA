"""
520. Detect Capital
link: https://leetcode.com/problems/detect-capital/description/
"""
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word==word.upper():
            return True
        else:
            return False
        