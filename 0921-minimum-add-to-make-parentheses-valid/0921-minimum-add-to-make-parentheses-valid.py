class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_brac = 0 
        min_add = 0 

        for ch in s:
            if ch == '(':
                open_brac += 1 
            else:
                if open_brac > 0:
                    open_brac -= 1 
                else:
                    min_add += 1 
        return min_add + open_brac