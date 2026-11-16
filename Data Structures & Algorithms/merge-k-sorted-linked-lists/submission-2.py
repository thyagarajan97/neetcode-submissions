# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Adding the less than and less-than or equal to dunder methods
class update_node:
    def __init__(self, node):
        self.node = node
    #end def
    def __lt__(self, other):
        if not isinstance(other, update_node):
            raise Exception(f'Error in type')
        else:
            return self.node.val < other.node.val
        #end if
    #end def
    def __lte__(self, other):
        if not isinstance(other, update_node):
            raise Exception(f'Error in type')
        else:
            return self.node.val <= other.node.val
        #end if
    #end def
#end class
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        head = None
        cur = None
        minHeap = []

        #Pushing the 1st element of all lists to the min-heap
        for llist in lists:
            if llist is not None:
                heapq.heappush(minHeap, update_node(llist))
            #end if
        #end for
        #Condition for creating the head of the linked list
        if minHeap:
            update_node_temp = heapq.heappop(minHeap)
            head = update_node_temp.node
            cur = update_node_temp.node
            if update_node_temp.node.next:
                heapq.heappush(minHeap, update_node(update_node_temp.node.next))
            #end if
        #end if
        while minHeap:
            update_node_temp = heapq.heappop(minHeap)
            cur.next = update_node_temp.node
            cur = cur.next
            if update_node_temp.node.next:
                heapq.heappush(minHeap, update_node(update_node_temp.node.next))
            #end if
        #end while
        return head


