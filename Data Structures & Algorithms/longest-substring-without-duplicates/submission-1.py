class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx = 0
        crnt = ''
        for char in s:
            if char not in crnt:
                crnt += char
                mx = max(mx, len(crnt))
            else:
                indx = crnt.index(char)
                crnt = crnt[indx+1:] + char
        return mx