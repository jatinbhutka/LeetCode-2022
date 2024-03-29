# 69. Sqrt(x):

"""
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

Example 1:
Input: x = 4
Output: 2

Example 2:
Input: x = 8
Output: 2

Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
Constraints:
0 <= x <= 231 - 1
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        return int(pow(x,0.5))
        
   
# Binary Search : 
# Time: O(Log N)
# Space: O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x
        
        left = 2
        right = x//2
        
        while left <= right:
            pivot = left + (right-left)//2
            num = pivot * pivot
            if num < x:
                left = pivot + 1
            elif num > x:
                right = pivot - 1
            else:
                return pivot
        return right
                
