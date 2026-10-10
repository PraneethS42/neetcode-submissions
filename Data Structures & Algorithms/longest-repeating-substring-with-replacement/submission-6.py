class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Move a sliding window
        # Keep moving it right while the length - most popular <= no. of replacements       
        l = 0 
        maxF = 0 # Store the max frequency as an integer
        count = {} # Map chars to their count
        res = 0

        for r in range(len(s)):
            # Add to our counts and update maxF
            count[s[r]] = 1 + count.get(s[r],0)
            maxF = max(maxF, count[s[r]])

            # Shift until it's valid
            while (r-l+1)-maxF > k:
                count[s[l]] -= 1
                # Why not update maxF to reduce it? Because we only 
                # want to consider new higher maximums for our result
                l+=1

            # Now we have a valid window, assess result
            res = max(res, r-l+1)

        return res