class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Move a sliding window
        # Keep moving it right while the length - most popular <= no. of replacements
        l,r = 0,0
        maxL = 0
        freq = {s[0]:1}

        while r < len(s):
            if ((r-l+1) - max(freq.values())) <= k:
                maxL = max(maxL, r-l+1)
                r += 1

                if r >= len(s):
                    break
                freq[s[r]] = 1 + freq.get(s[r], 0)

            else:
                freq[s[l]] -= 1
                l += 1
        return maxL