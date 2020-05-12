# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #Iterative Approach
        prevNode = head
        iterNode = head
        while iterNode != None:
            if iterNode == head:
                iterNode = prevNode.next
                prevNode.next = None
            else:
                temp_iterNode = iterNode.next
                iterNode.next = prevNode
                prevNode = iterNode
                iterNode = temp_iterNode
        head = prevNode
        return(head)
        
