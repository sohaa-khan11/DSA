"""
520. Detect Capital
link: https://leetcode.com/problems/detect-capital/description/
"""
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()