"""
1470. Shuffle the Array
=========================

Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

 

Example 1:

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
Example 2:

Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]
Example 3:

Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]

"""

# Solution 1:

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ret = [None] * 2 * n
        i = 0
        j = n
        k = 0
        while i < n:
            ret[k] = nums[i]
            ret[k+1] = nums[j]
            i = i + 1
            j = j + 1
            k = k + 2
        return ret
      
# Time - O(N)
# Space - O(N)


# Solution 2: optimized Approach - Methametical 

"""
Input: nums = [2,5,1,3,4,7], n = 3

Steps:
 - Multiply nth to the last th element by 10^4 + ith
 - Use Quotent and Reminder for Getting final array
nums = 
Output: [2,3,5,4,1,7] 
"""

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        j = 0
        for i in range(n,n*2):
            nums[i] = 10000 * nums[i] + nums[j]
            j = j+1
        k = n
        for i in range(0,n*2):
            if i%2 == 0:
                nums[i] = nums[k]%10000
            else:
                nums[i] = nums[k]//10000
                k += 1  
        return nums
            

# Time - O(N)
# Space - O(1)





# Solution 2: optimized Approach - Divide and Conquer:
# this solution is only for 2^n Number of elements (4,8,16...)


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        def divide_con (arr, first, last):
            if first >= last:
                return
            if last - first == 1:
                return

            mid = (last + first)//2
            temp = mid + 1
            next_mid = (mid + first) // 2

            for i in range(next_mid+1, mid+1):
                arr[i], arr[temp] = arr[temp],arr[i]
                temp += 1
            divide_con (arr, first, mid)
            divide_con(arr, mid+1, last)
        
        
        divide_con (nums, 0, (2*n) -1)
        return nums

# Time - O(N Log N)
# Space - O(1)





# Solution 4:   
    
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []

        for i in range(n):
            arr += [ nums[i], nums[i + n] ]

        return arr
       
# Time - O(N)
# Space - O(N)       
       
