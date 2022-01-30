"""
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.

 

Example 1:

Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
Example 2:

Input: nums = [2,3]
Output: [2,3]
 

Constraints:

2 <= nums.length <= 2 * 104
nums.length is even.
Half of the integers in nums are even.
0 <= nums[i] <= 1000
 

Follow Up: Could you solve it in-place?
"""



# Solution1: Using two pointer from each end
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = 0
        odd = len(nums) - 1
        while even < len(nums) and odd > 0:
            if nums[even] % 2 == 0:
                even += 2
            elif nums[odd] % 2 != 0:
                odd -= 2
            else:
                nums[even], nums[odd] = nums[odd],nums[even]
                even += 2
                odd -= 2
        return nums
        
# Time: O(N)
# Space: O(1)


# Solution2: Using 2 new odd, even array
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        j = 0
        i = 0
        while i < len(nums):
            nums[i] = even[j]
            nums[i+1] = odd[j]
            i += 2
            j += 1
        return nums
# Time: O(N)
# Space: O(N)      
        
