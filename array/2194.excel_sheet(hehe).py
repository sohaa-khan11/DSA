"""  
2194. Cells in a Range on an Excel Sheet
link: https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/description/
"""
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        s = s.split(":")
        start, end = s[0], s[1]
        
        start_col, start_row = start[0], int(start[1:])
        end_col, end_row = end[0], int(end[1:])
        
        result = []
        
        for col in range(ord(start_col), ord(end_col) + 1):
            for row in range(start_row, end_row + 1):
                result.append(chr(col) + str(row))
        
        return result