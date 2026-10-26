class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""
        min_len = min(len(s) for s in strs)
        if min_len == 0:
            return longest_prefix
        
        for i in range(min_len):
            for s in strs:
                if s[i] != strs[0][i]:
                    return strs[0][:i]

        return strs[0][:min_len]
        
            
