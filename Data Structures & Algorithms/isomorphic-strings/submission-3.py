class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_dict = {}
        char_rev_dict = {}
        if not s and not t:
            return True
        if len(s) != len(t):
            return False
        for index in range(len(s)):
            if char_dict.get(s[index]):
                if char_dict[s[index]] != t[index]:
                    return False
                #end if
            else:
                char_dict[s[index]] = t[index]
                if char_rev_dict.get(t[index]): 
                    if char_rev_dict[t[index]] != s[index]:
                        return False
                else:
                    char_rev_dict[t[index]] = s[index]
            #end if
        #end for
        return True