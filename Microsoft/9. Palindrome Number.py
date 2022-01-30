"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""


# Solution1: Using String Method on Int.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
# Time: O(N)
# Space: 



# Solution2: Using % and // Method:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        oldnum = x
        rev = 0
        while x > 0:
            rev = rev * 10 + x%10
            x = x//10
        return rev == oldnum
      
      
      
# Solution2: Using % and // Method:

"""
So, instead of reversing the whole integer, let's convert half of the integer and then check if it's palindrome.
But we don't know when is that half going to come.

Example, if x = 15951, then let's create reverse of x in loop. Initially, x = 15951, revX = 0

x = 1595, revX = 1
x = 159, revX = 15
x = 15, revX = 159
We see that revX > x after 3 loops and we crossed the half way in the integer bcoz it's an odd length integer.
If it's an even length integer, our loop stops exactly in the middle.

Now we can compare x and revX, if even length, or x and revX//10 if odd length and return True if they match.
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x>0 and x%10 ==0):
            return False
        
        result = 0
        while x>result:
            result = 10*result + x%10
            x = x//10
        if x==result or x == result//10:
            return True
        else:
            return False
                  



