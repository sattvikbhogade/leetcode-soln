class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        i = 0
        j = 0
        ans = 0
        m = {}
    
        while j < n:
            if fruits[j] in m:
                m[fruits[j]] += 1
            else:
                m[fruits[j]] = 1
    
            while len(m) > 2:
                m[fruits[i]] -= 1
                if m[fruits[i]] == 0:
                    del m[fruits[i]]
                i += 1
    
            ans = max(ans, j - i + 1)
            j += 1
    
        return ans