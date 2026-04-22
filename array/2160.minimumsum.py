"""
2160. Minimum Sum of Four Digit Number After Splitting Digits
link: https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/description/
"""
class Solution:
    def minimumSum(self, num: int) -> int:
        num = list(str(num))
        num.sort()
        new1=int(num[0]+num[2])
        new2=int(num[1]+num[3])
        return new1+new2
        