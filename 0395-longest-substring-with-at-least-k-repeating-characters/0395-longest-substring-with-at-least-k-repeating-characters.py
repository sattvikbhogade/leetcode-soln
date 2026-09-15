class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0

        for uniqueTarget in range(1, 27):
            i = 0
            j = 0
            m = {}
            unique = 0
            valid = 0

            while j < n:
                if s[j] not in m:
                    m[s[j]] = 0
                    unique += 1

                m[s[j]] += 1

                if m[s[j]] == k:
                    valid += 1

                while unique > uniqueTarget:
                    m[s[i]] -= 1

                    if m[s[i]] == k - 1:
                        valid -= 1

                    if m[s[i]] == 0:
                        del m[s[i]]
                        unique -= 1

                    i += 1

                if unique == valid:
                    ans = max(ans, j - i + 1)

                j += 1

        return ans