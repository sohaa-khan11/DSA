"""
1812. Determine Color of a Chessboard Square
link: https://leetcode.com/problems/determine-color-of-a-chessboard-square/description/
"""
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x = ord(coordinates[0]) - ord('a') + 1
        y= int(coordinates[1])
        if (x+y)%2==0:
            return False
        else:
            return True
        

        