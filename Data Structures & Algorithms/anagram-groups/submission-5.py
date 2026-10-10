class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(m*n) time and O(m) space, n is length of longest str
        # Group all of the same ones tgt
        result = defaultdict(list)
        for word in strs:
            sortedString = ''.join(sorted(word))
            result[sortedString].append(word)
        # Will print all of the values (which are lists) as a total list
        return list(result.values())
