class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Conditions -> len(s1) <= len(s2)
        # Sliding window can be same size as size of s1
        if len(s1) > len(s2):
            return False

        count = [0]*26
        for char in s1:
            count[ord(char)-ord('a')] += 1

        # The naive approach initially was to create a hash map for each substring and
        # compare but thats still O(n) (well I guess O(26)) for n times

        # Start by matching length
        for i in range(len(s1)):
            count[ord(s2[i])-ord('a')] -= 1

        if all(val == 0 for val in count):
            return True

        for i in range(len(s1), len(s2)):
            count[ord(s2[i-len(s1)])-ord('a')] += 1
            count[ord(s2[i])-ord('a')] -= 1
            if count[ord(s2[i])-ord('a')] == 0 and all(val == 0 for val in count):
                return True
    
        return False

        
        