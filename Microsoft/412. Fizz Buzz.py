# 412. Fizz Buzz:

"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 

Example 1:
Input: n = 3
Output: ["1","2","Fizz"]

Example 2:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Example 3:
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

Constraints:
1 <= n <= 104
"""


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = []
        for i in range(1, n+1):
            if i%3 == 0 and i%5 == 0:
                ret.append("FizzBuzz")
            elif i%3 == 0:
                ret.append("Fizz")
            elif i%5 == 0:
                ret.append("Buzz")
            else:
                ret.append(str(i))
        return ret
      
      
# Complexity Analysis:
# Time Complexity: O(N)O(N)
# Space Complexity: O(1)O(1)
  
  
  
  
  
  
  
"""
Intuition

This approach is an optimization over approach 2. When the number of mappings are limited, approach 2 looks good. But what if you face a tricky interviewer and he decides to add too many mappings?

Having a condition for every mapping is not feasible or may be we can say the code might get ugly and tough to maintain.

What if tomorrow we have to change a mapping or may be delete a mapping? Are we going to change the code every time we have a modification in the mappings?

We don't have to. We can put all these mappings in a Hash Table.

Algorithm

Put all the mappings in a hash table. The hash table fizzBuzzHash would look something like { 3: 'Fizz', 5: 'Buzz' }
Iterate on the numbers from 1 ... N1...N.
For every number, iterate over the fizzBuzzHash keys and check for divisibility.
If the number is divisible by the key, concatenate the corresponding hash value to the answer string for current number. We do this for every entry in the hash table.
Add the answer string to the answer list.

"""
  
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # ans list
        ans = []

        # Dictionary to store all fizzbuzz mappings
        fizz_buzz_dict = {3 : "Fizz", 5 : "Buzz"}

        for num in range(1,n+1):

            num_ans_str = ""

            for key in fizz_buzz_dict.keys():

                # If the num is divisible by key,
                # then add the corresponding string mapping to current num_ans_str
                if num % key == 0:
                    num_ans_str += fizz_buzz_dict[key]

            if not num_ans_str:
                num_ans_str = str(num)

            # Append the current answer str to the ans list
            ans.append(num_ans_str)  

        return ans
