#Need a doubly linked list
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    #end def
#end class

class LRUCache:    
    def __init__(self, capacity: int):
        self.lookup_dict = dict() #To look up in O(1)
        #Left and right pointers dummy nodes, left = LRU, right = MRU
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        self.capacity = capacity
    #end def

    #helper function to insert a node at the right of the DLL
    def insert_at_end(self, Node):
        rp = self.right.prev
        r = self.right
        rp.next = Node
        Node.prev = rp
        Node.next = r
        r.prev = Node
    #end def

    def delete_Node(self, Node):
        p = Node.prev
        n = Node.next
        p.next = n
        n.prev = p
    #end def delete_Node

    def get(self, key: int) -> int:
        if self.lookup_dict.get(key) is None:
            return -1
        #Getting element from hash-map
        node = self.lookup_dict[key]
        ret_val = node.val
        #First remove the element from middle of dll
        self.delete_Node(node)
        #Insert Element to end of dll 
        self.insert_at_end(node)
        return ret_val
    #end def

    def put(self, key: int, value: int) -> None:
        if self.lookup_dict.get(key) is None:
            #First time insert
            #Create a node
            obj = Node(key, value)
            #insert at end
            self.insert_at_end(obj)
            self.lookup_dict[key] = obj
        else:
            #Updation
            #Get the node
            node = self.lookup_dict[key]
            #Update node value
            node.val = value
            #First remove the element from middle of dll
            self.delete_Node(node)
            #Insert Element to end of dll 
            self.insert_at_end(node)
        #end if
        #Check if len > cap
        if len(self.lookup_dict) > self.capacity:
            #Need to remove the left-most element
            node = self.left.next
            del self.lookup_dict[node.key]
            #Remove the element from middle of dll
            self.delete_Node(node)
            del node
        #end if





