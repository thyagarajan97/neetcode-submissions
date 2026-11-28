# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Traverse till end of list to get count
        node_count = 1
        cur = head
        while cur.next:
            node_count+=1
            cur = cur.next
        #end while
        node_num_to_remove = node_count - n + 1
        #print(f'node_count: {node_count}, node_number to remove: {node_num_to_remove}')
        #Remove from start, or remove from end or remove from middle
        if node_count == n: #Removing from start
            #Advance the head-pointer if it exists
            if head.next:
                return head.next
            return None
        cur = head
        node_count_2 = 1
        while cur.next:
            if node_count_2 + 1 == node_num_to_remove:
                if cur.next.next:
                    #Removing node from somewhere in between
                    cur.next = cur.next.next
                    return head
                else:
                    #removing the last-node
                    cur.next = None
                    return head
            cur = cur.next
            node_count_2+=1
        #end while
    #end def

        