"""
1486. XOR Operation in an Array
link: https://leetcode.com/problems/xor-operation-in-an-array/description/
"""
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        ans=0
        for i in range(n):
            nums.append(start+2*i)
        for x in nums:
            ans=ans^x
        return ans
