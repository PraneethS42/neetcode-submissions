class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Iterate through s, make a map then delete?
        if len(s) != len(t):
            return False
        char_dict = {}
        for char in s:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        for char in t:
            if char in char_dict:
                char_dict[char] -= 1
                if char_dict[char] < 0:
                    return False
            else:
                return False
        return True
          