from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        char_freq = defaultdict(int)
        max_len_str = 1
        for r in range(len(s)):
            char_freq[s[r]]+=1
            max_freq_char = max(char_freq.values())
            #Find the max-freq str
            if (r-l+1) - max_freq_char <= k:
                max_len_str = max(r-l+1, max_len_str)
            while (r-l+1) - max_freq_char > k:
                max_freq_char = max(char_freq.values())
                char_freq[s[l]]-=1
                l+=1
            #end while
        #end for
        return max_len_str