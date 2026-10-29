class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_dict = {}
        char_rev_dict = {}
        if not s and not t:
            return True
        if len(s) != len(t):
            return False
        for index, char in enumerate(s):
            if char_dict.get(char):
                if char_dict[char] != t[index]:
                    return False
                #end if
            else:
                char_dict[char] = t[index]
                if char_rev_dict.get(t[index]): 
                    if char_rev_dict[t[index]] != char:
                        return False
                else:
                    char_rev_dict[t[index]] = char
            #end if
        #end for
        return True