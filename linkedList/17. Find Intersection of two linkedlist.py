# 160. Intersection of Two Linked Lists



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Solution 1: (Using difference of node counts) 
"""
- Get count of the nodes in the first list, let count be c1.
- Get count of the nodes in the second list, let count be c2.
- Get the difference of counts d = abs(c1 – c2)
- Now traverse the bigger list from the first node till d nodes so that from here onwards both the lists have equal no of nodes
- Then we can traverse both the lists in parallel till we come across a common node. (Note that getting a common node is done by comparing the address of the nodes)
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        # Find Len of headA
        la = 0
        currA = headA
        while currA:
            la += 1
            currA = currA.next
            
        # Find Len of headB
        lb = 0
        currb = headB
        while currb:
            lb += 1
            currb = currb.next 
        
        # Find diff between la and lb:
        l = abs(la-lb)
        
        #travel extra dist:
        currA = headA
        currB = headB
        if la > lb:
            while l>0:
                l -= 1
                currA = currA.next
        if lb > la:
            while l:
                l -= 1
                currB = currB.next
        
        # Find Intersection
        while currA and currB:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next
        
        return None
            
        
# Time: O(N)
# Space: O(1)



# Solution 2:  Genius Method

"""
It only goes through A and B once.
Let's say:
headA = A + O
headB = B + O
where O is the repeated part.
To get to O from headA, the length is A + O + B,
to get to O from headB, the length is B + O + A
"""

'''
Using Two pointers : 

- Initialize two pointers ptr1 and ptr2  at the head1 and  head2.
- Traverse through the lists,one node at a time.
- When ptr1 reaches the end of a list, then redirect it to the head2.
- similarly when ptr2 reaches the end of a list, redirect it the head1.
- Once both of them go through reassigning, they will be equidistant from 
 the collision point
- If at any node ptr1 meets ptr2, then it is the intersection node.
- After second iteration if there is no intersection node it returns NULL.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        currA = headA
        currB = headB
        while currB != currA:
            if currA:
                currA = currA.next
            else:
                currA = headB
            
            if currB:
                currB = currB.next
            else:
                currB = headA
        return currA
      
# Time: O(N)
# Space: O(1)



'''
Method 3 (Simply use two loops) :
Use 2 nested for loops. The outer loop will be for each node of the 1st list and inner loop will be for 2nd list. In the inner loop, check if any of nodes of the 2nd list is same as the current node of the first linked list. The time complexity of this method will be O(M * N) where m and n are the numbers of nodes in two lists.

Method 4 (Mark Visited Nodes) :
This solution requires modifications to basic linked list data structure. Have a visited flag with each node. Traverse the first linked list and keep marking visited nodes. Now traverse the second linked list, If you see a visited node again then there is an intersection point, return the intersecting node. This solution works in O(m+n) but requires additional information with each node. A variation of this solution that doesn’t require modification to the basic data structure can be implemented using a hash. Traverse the first linked list and store the addresses of visited nodes in a hash. Now traverse the second linked list and if you see an address that already exists in the hash then return the intersecting node.

'''



