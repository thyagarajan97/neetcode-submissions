class MinStack:
    #This solution optimizes it further to use O(1) space instead of 2 stacks
    def __init__(self):
        self.stack = []
        self.min_val = float('inf')
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_val = val
            self.stack.append(val)
        else:
            #Do we encode or not
            if val < self.min_val:
                # Encode the old minimum into a value smaller than the new min
                encoded = 2 * val - self.min_val
                self.stack.append(encoded)
                self.min_val = val
            else:
                self.stack.append(val)
        #end if

    def pop(self) -> None:
        val = self.stack.pop()
        if val < self.min_val: #Encoded val
            #Need to decode and update min_val
            self.min_val = (2*self.min_val - val)
        #end if

    def top(self) -> int:
        val  = self.stack[-1]
        if val < self.min_val: # Encoded val
            #Decoded value is just the min_itself
            val = self.min_val
        #end if
        return val

    def getMin(self) -> int:
        return self.min_val
