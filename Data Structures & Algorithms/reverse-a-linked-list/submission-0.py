# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node, current_node = None, head 
        while current_node:
            temp = current_node #Caching the existing curr-pointer
            current_node = current_node.next #Moving the current-pointer
            #Before moving the prev-pointer we need to establish the link to prev
            temp.next = prev_node 
            prev_node = temp
            #print(f'prev_node = {prev_node.val}, ', end="")
            # if current_node:
            #     print(f'curr-node: {current_node.val}')
        #end while
        return prev_node
    #end def reverseList

