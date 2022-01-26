"""
1512. Number of Good Pairs

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""


# Solution 1: Brute Force:

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count+=1
        return count

# Time - O(N^2)
# Space - O(1)



# Solution 2: Using hash Table:

"""
Fundamental Math Concept (Combinations)
The "# of pairs" can be calculated by summing each value from range 0 to n-1, where n is the "# of times repeated". So the "# of pairs" for the 5 repeated values, would be 0+1+2+3+4 = 10.

Another way to think about it is:

Notice in the table below how the number of pairs increments by adding the previous "# of times repeated" to the previous "# of pairs."

For example: to get the "# of pairs" for 3 repeated values, you would add the previous "# of times repeated" (which is 2) with the previous "# of pairs" (which is 1). Therefore, the "# of pairs for 3 repeated values is 2+1=3. In this method, you don't peform the same computations multiple times.

Example Table of # of repeated items with their corresponding # of pairs

# of times repeated	  |     # of pairs
2	                    |       1
3	                    |       3
4	                    |       6
5	                    |       10
6	                    |       15


First we can count the frequency of each numbers using array. If a number appears n times, then n * (n – 1) / 2 pairs can be made with this number.



"""
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash_tabel = {}
        
        for i in range(len(nums)):
            if nums[i] in hash_tabel:
                hash_tabel[nums[i]] = hash_tabel[nums[i]] + 1
            else:
                hash_tabel[nums[i]] = 1

                
        good_pair = 0
        
        for key, val in hash_tabel.items():
            if val > 1:
                good_pair += val * (val-1)//2
                
        return good_pair

# Time - O(N)
# Space - O(N)








# Solution 3: Using hash Map 

# [1,1,1] = 2 + 1 = 3
# [1,1,1,1] = 3 + 2 + 1 = 6
# Thats, Res = res + hash[number], hash[number] += 1

# If the value already exists in the hashMap that means the number of new pairs is equal to the frequency since the current value can be paired with each prior occurrence .



class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash = {}
        res = 0    
        for number in nums:
            if number in hash:
                res+=hash[number]
                hash[number]+=1
            else:
                hash[number]=1
        return res
      
# Time - O(N)
# Space - O(N)      
