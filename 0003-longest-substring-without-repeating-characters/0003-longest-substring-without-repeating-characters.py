class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            n = len(s)
            i = 0
            j = 0
            ans = 0
            m = {}

            while j < n:
                m[s[j]] = m.get(s[j], 0) + 1

                while m[s[j]] > 1:
                    m[s[i]] -= 1

                    if m[s[i]] == 0:
                        del m[s[i]]

                    i += 1

                ans = max(ans, j - i + 1)

                j += 1

            return ans
