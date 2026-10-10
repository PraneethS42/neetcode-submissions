class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Second solution - sorting
        word_to_sort = defaultdict(list) # Lets us append without worrying of edge case of empty list
        for word in strs:
            # Ensure the sorted doesn't return blank array by adding to join nothing
            sortedWord = ''.join(sorted(word)) 
            # Append this word to other words that have the same sorted form
            word_to_sort[sortedWord].append(word)
        # Return a list of just the values, don't need the keys 
        return list(word_to_sort.values())
