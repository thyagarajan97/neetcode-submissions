def add_val_to_node(node, val):
    #Helper function which will add a Node's val with a carry bit and generate the carry + updated node
    carry = 0
    if node.val + val > 9:
        node = ListNode((node.val + val)%10)
        carry = 1
    else:
        node = ListNode(node.val + val)
    return (node, carry)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret_head = ListNode(0,None)
        cur = ret_head
        carry = 0
        while l1 and l2:
            (node, carry) = add_val_to_node(l1, l2.val + carry)
            cur.next = node
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        #end while
        #print(f'Current-Result: {ret_head}, carry = {carry}')
        #Need to handle left-over carry + remaining node
        if l1 is not None:
            #print('l2 is empty')
            #end of list of l2
            while l1:
                (node, carry) = add_val_to_node(l1, carry)
                cur.next = node
                cur = cur.next
                l1 = l1.next
            #end while
        #end if
        if l2 is not None:
            #print('l1 is empty')
            #end of list of l1
            while l2:
                (node, carry) = add_val_to_node(l2, carry)
                cur.next = node
                l2 = l2.next
                cur = cur.next
            #end while
        #end if  
        if l1 is None and l2 is None and carry != 0:
            cur.next = ListNode(carry)
        #end if      
        return ret_head.next
    #end def
#end class
