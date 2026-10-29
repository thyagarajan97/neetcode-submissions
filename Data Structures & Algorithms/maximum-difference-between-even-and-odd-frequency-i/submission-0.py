class Solution:
    def maxDifference(self, s: str) -> int:
        from collections import Counter
        freq_dict = Counter(s)
        print(freq_dict)
        even_val = 1001
        odd_val = -1
        for value in freq_dict.values():
            if value % 2 == 0:
                even_val = min(even_val, value)
            else:
                odd_val = max(odd_val, value)
            #end if
        #end for
        return (odd_val - even_val)