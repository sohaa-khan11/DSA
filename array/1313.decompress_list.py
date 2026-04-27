"""
1313. Decompress Run-Length Encoded List
link: https://leetcode.com/problems/decompress-run-length-encoded-list/description/
"""
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output=[]
        for i in range(0, len(nums), 2):
            [freq, val] = [nums[i], nums[i+1]]
            for _ in range(freq):
                output.append(val)
        return output
            

        