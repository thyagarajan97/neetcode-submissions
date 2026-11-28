# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def get_right_node(self, head) -> ListNode:
        cur = head
        r = cur
        while cur.next:
            r = cur
            cur = cur.next
        #cur-pointer is pointing to the end-1 of the ll
        #Removes the node from the end of the ll and returns it
        r.next = None #Setting n-1 to point to None
        return cur
    #end def

    def insert_node_after_node(self, node, insert_node):
        #1->3 need to insert 2 to get 1->2->3
        temp = node.next
        node.next = insert_node
        insert_node.next = temp
    #end def


    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return
        l = head
        #R-pointer is pointing to the end-1 of the ll
        while l.next is not None and l.next.next is not None:
            last_node = self.get_right_node(l)
            self.insert_node_after_node(l, last_node)
            l = l.next.next
            #print(root)
        #end while
        