"""
412. Fizz Buzz
link: https://leetcode.com/problems/fizz-buzz/
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        hehe=[]
        for i in range (1, n+1):
            if i%3==0 and i%5==0:
                hehe.append("FizzBuzz")
            elif i%3==0:
                hehe.append("Fizz")
            elif i%5==0:
                hehe.append("Buzz")
            else:
                hehe.append(str(i))
        return hehe
            
        