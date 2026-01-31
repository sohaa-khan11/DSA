'''
2413. Smallest Even Multiple
link: https://leetcode.com/problems/smallest-even-multiple/description/

answer:

'''
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2!=0:
            return 2*n
        if n%2==0:
            return n