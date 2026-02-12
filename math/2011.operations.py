'''
2011. Final Value of Variable After Performing Operations
link: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/

answers:
'''
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for ch in operations:
            if '++' in ch:
                x+=1
            else:
                x-=1
        return x     

