# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #Recursive Approach
        currentNode = head
        if currentNode is not None and currentNode.next is not None:
            revHead = Solution.reverseList(self, currentNode.next)
            currentNode.next.next = currentNode
            currentNode.next = None
            return(revHead)
        else:
            revHead = currentNode
            return(revHead)
        
        
