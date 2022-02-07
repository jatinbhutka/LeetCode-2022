
# 147. Insertion Sort List:

'''
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.


![image](https://user-images.githubusercontent.com/35987583/152753896-af464080-c6e8-4199-812f-763b758f60b2.png)

![image](https://user-images.githubusercontent.com/35987583/152753918-faf91671-4604-4cb3-a8dc-fc73c5e5a54c.png)

![image](https://user-images.githubusercontent.com/35987583/152753939-8e0bd9b1-2255-4ec5-9dbe-5a7c62801bbd.png)

Constraints:

The number of nodes in the list is in the range [1, 5000].
-5000 <= Node.val <= 5000
'''

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = start = ListNode(-50000)
        prev.next = head
        curr = head
        while curr.next != None :
            if curr.next.val < curr.val:
                while prev.next.val < curr.next.val:
                    prev = prev.next
                temp = prev.next
                prev.next = curr.next
                curr.next = curr.next.next
                prev.next.next = temp
                prev = start
            else:
                curr = curr.next
                
        return start.next
      

# Time: O(N^2)
# Space: O(1)     
        
