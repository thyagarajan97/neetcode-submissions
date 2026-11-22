class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        #end for
        from collections import Counter, defaultdict
        t_char_map = Counter(t)
        s_map = defaultdict(int)
        l = 0
        min_val = float('inf')
        formed_cnt = 0
        reqd_cnt = len(t_char_map)
        window_len = 0 
        best_l = 0
        best_r = 0
        #print(t_char_map)
        for r in range(len(s)):
            s_map[s[r]]+=1 #Expanding the window
            window_len = r-l+1
            if s_map[s[r]] == t_char_map[s[r]]:
                formed_cnt+=1
            #print(f'inserting: {s[r]}, l = {l}, r = {r}')
            while formed_cnt == reqd_cnt:
                #print(f's_map and t_char_map matched: {s[l:r+1]}, {window_len}')
                #print(f'removing: {s[l]}, l = {l}, r = {r}, {s_map}')
                #min_val = min(window_len, min_val)
                if window_len < min_val:
                    min_val = window_len
                    best_l = l
                    best_r = r
                    #print(window_str)
                #end if
                s_map[s[l]] -= 1
                if s_map[s[l]] < t_char_map[s[l]]:
                    formed_cnt-=1
                #Keep shrinking the window
                l+=1
                window_len = r-l+1
            #end while
        #end for
        return "" if min_val == float("inf") else s[best_l : best_r + 1]
    #end def
#end Solution
