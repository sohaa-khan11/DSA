"""
58. Length of Last Word
link: https://leetcode.com/problems/length-of-last-word/description/
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        count =0
        for i in range(len(s) - 1, -1, -1):
            if s[i]==" ":
                break
            count+=1
        return count
        