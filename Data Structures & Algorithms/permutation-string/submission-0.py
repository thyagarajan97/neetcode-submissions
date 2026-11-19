def get_str_hash(string):
    hash_val = 0
    for char in string:
        hash_val += hash(char)
    return hash_val
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_val = get_str_hash(s1)
        l = 0
        r = 0
        #size of s1
        window_size = len(s1)
        #print(window_size)
        r = window_size - l -1
        while r < len(s2):
            #print(s2[l:r+1])
            if hash_val == get_str_hash(s2[l:r+1]):
                return True
            #end if
            l+=1
            r+=1
        #end while
        return False