class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        stack = []
        def dfs(i):
            if i>n:
                if len(stack) == k:
                    result.append(stack.copy())
                return 
            #Add element
            stack.append(i)
            dfs(i+1)
            stack.pop()
            dfs(i+1)
        #end def
        dfs(1)
        return result