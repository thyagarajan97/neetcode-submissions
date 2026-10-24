class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Remove non-alphanumeric chars
        new_str = ''
        for char in s:
            if char.isalnum():
                new_str += char.lower()
            #end if
        #end for
        r = len(new_str) - 1
        for index, l in enumerate(new_str):
            if l != new_str[r]:
                return False
            if (index > len(new_str)) // 2:
                break
            r-=1
            #end if 
        #end for
        return True

            