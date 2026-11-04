class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        from collections import Counter
        freq_dict = Counter(arr)
        for key, value in freq_dict.items():
            if value == 1:
                k-=1
                if k==0:
                    return key
                #end if
            #end if
        #end for
        return ""