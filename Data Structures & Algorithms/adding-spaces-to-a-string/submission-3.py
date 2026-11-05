class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        #new_str = ""
        count = 0
        l1 = []
        #Inefficient
        l = 0
        r=0
        for r in spaces:
            l1.append(s[l:r])
            l1.append(" ")
            l=r
            #print(l1)
            #print(f'Current-string: {s}, index: {index}')
        #end for
        l1.append(s[l:])
        #print(l1)
        return "".join(l1)
