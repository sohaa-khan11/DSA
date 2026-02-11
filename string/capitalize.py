"""
2129. Capitalize the Title
link: https://leetcode.com/problems/capitalize-the-title/description/
"""
class Solution:
    def capitalizeTitle(self, title: str) -> str:
         words=title.lower().split()
         result=[]
         for word in words:
            if len(word) <= 2:
                result.append(word)
            else:
                result.append(word.capitalize())

         return " ".join(result)