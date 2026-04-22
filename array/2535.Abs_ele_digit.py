"""
2535. Difference Between Element Sum and Digit Sum of an Array
link: https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/
"""
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element = sum(nums)
        
        digit = 0
        for i in nums:
            for j in str(i):
                digit += int(j)
        
        return abs(element - digit)