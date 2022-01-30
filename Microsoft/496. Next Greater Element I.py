"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Constraints:

0 <= n <= 30
"""

# Solution1: Recursive

class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        return self.fib(n-1) + self.fib(n-2)

      
# Time: O()
# Space: O()


# Solution1: Reduce recursive call using Memoization
class Solution:

    def fib(self, n: int) -> int:
        memo = {}
        memo[0] = 0
        memo[1] = 1
        def fib_memo(n):
            if n in memo: 
                return memo[n]
            else: 
                memo[n] = fib_memo(n-1)+fib_memo(n-2)
            return memo[n]
        return fib_memo(n)      
# Time: O(N)
# Space: O(N)



# Solution1: Reduce recursive call using Memoization
class Solution:
    memo = {}
    def fib(self, N: int) -> int:
        if N == 0: return 0
        if N == 1: return 1
        if N-1 not in self.memo: self.memo[N-1] = self.fib(N-1)
        if N-2 not in self.memo: self.memo[N-2] = self.fib(N-2)
        return self.memo[N-1]+self.memo[N-2]      
# Time: O()
# Space: O()



# Solution1: Iterativi Method using Memoization
class Solution:
    def fib(self, n: int) -> int:
        memo = [0, 1]
        for i in range(2, n+1):
            memo.append(memo[i-1]+memo[i-2])
        return memo[n] 
# Time: O(N)
# Space: O(N)      

      
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        memo = [0, 1]
        for i in range(2, n+1):
            memo = [memo[-1], memo[-1]+memo[-2]]
        return memo[-1]      
      
# Time: O(N)
# Space: O(1)
      

