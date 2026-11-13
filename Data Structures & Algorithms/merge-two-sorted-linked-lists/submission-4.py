# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        l3_curr = None
        l3_head = None
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        while l1 and l2:
            if l1.val <= l2.val:
                node = l1
                l1 = l1.next
                #print('Adding l1')
            else:
                node = l2
                l2 = l2.next
                #print('Adding l2')
            #end if
            if l3_curr:
                l3_curr.next = node
                l3_curr = l3_curr.next
            else:
                #print('Creating Head')
                l3_head = node
                l3_curr = l3_head
        #end while
        #If l1 is exhausted
        if not l1:
            l3_curr.next = l2
        #end if
        if not l2:
            l3_curr.next = l1
        #end if
        return l3_head
