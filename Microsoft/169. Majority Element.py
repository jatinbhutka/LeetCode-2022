"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1
 

Follow-up: Could you solve the problem in linear time and in O(1) space?

"""


# Solution 1: Using hash map:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        for i in range(len(nums)):
            if nums[i] in hash:
                hash[nums[i]] += 1
            else:
                hash[nums[i]] = 1
        for key, val in hash.items():
            if val > len(nums)/2:
                return key
              
              
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        for i in range(len(nums)):
            if nums[i] in hash:
                hash[nums[i]] += 1
            else:
                hash[nums[i]] = 1
            if hash[nums[i]] > len(nums)//2:
                return nums[i]              

# Time : O(N)
# Space : O(N)



# Solution 2: Using Sorting and The majority element is the element that appears more than ⌊n / 2⌋ times.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

# Time : O(N LogN)
# Space : O(1)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        
        if len(nums) == 1:
            return nums[0]
        
        count = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            if count > len(nums)/2:
                return nums[i]
            if nums[i] != nums[i-1]:
                count = 1
                
# Time : O(N LogN)
# Space : O(1)







# Solution 3: Using majority element running count (+ and -):
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        count = 1
        
        for i in range(1,len(nums)):
            if majority == nums[i]:
                count += 1
            if majority != nums[i]:
                count -= 1
            if count == 0:
                majority = nums[i]
                count += 1
        return majority

# Time : O(N)
# Space : O(1)


