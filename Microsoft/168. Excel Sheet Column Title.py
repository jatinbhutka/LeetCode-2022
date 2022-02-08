# 168. Excel Sheet Column Title:


'''
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:
Input: columnNumber = 1
Output: "A"

Example 2:
Input: columnNumber = 28
Output: "AB"

Example 3:
Input: columnNumber = 701
Output: "ZY"
 
Constraints:
1 <= columnNumber <= 231 - 1
'''

'''
Let's see the relationship between the Excel sheet column title and the number:

A   1     AA    26+ 1     BA  2×26+ 1     ...     ZA  26×26+ 1     AAA  1×26²+1×26+ 1
B   2     AB    26+ 2     BB  2×26+ 2     ...     ZB  26×26+ 2     AAB  1×26²+1×26+ 2
.   .     ..    .....     ..  .......     ...     ..  ........     ...  .............   
.   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
.   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
Z  26     AZ    26+26     BZ  2×26+26     ...     ZZ  26×26+26     AAZ  1×26²+1×26+26
Now we can see that ABCD＝A×26³＋B×26²＋C×26¹＋D＝1×26³＋2×26²＋3×26¹＋4

But how to get the column title from the number? We can't simply use the n%26 method because:

ZZZZ＝Z×26³＋Z×26²＋Z×26¹＋Z＝26×26³＋26×26²＋26×26¹＋26

We can use (n-1)%26 instead, then we get a number range from 0 to 25.
'''


class Solution:
    def convertToTitle(self, n: int) -> str:
        abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans=""
        while n:
            n = n - 1
            ans=abc[n%26]+ans
            n=n//26
        return ans
      

def convertToTitle(self, n):
    r = ''
    while(n>0):
        n -= 1
        r = chr(n%26+65) + r
        n /= 26
    return r      
