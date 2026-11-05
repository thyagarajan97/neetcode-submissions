class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        l1 = [] #Holds the string spliced into sections
        #Creating a new-string each-time is inefficient
        #Using 2 pointers l and r, l points to start of string, r points to the place where space needs to be inserted
        l = 0
        r = 0
        for r in spaces:
            l1.append(s[l:r])
            l1.append(" ")
            l=r
        #end for
        l1.append(s[l:])
        return "".join(l1)
