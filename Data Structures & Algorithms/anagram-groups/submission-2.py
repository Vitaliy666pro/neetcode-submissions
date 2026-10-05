class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Time is O(n · k log k), where n is the number of words and k is
         the maximum word length — for each word we sort its characters.
         Space is O(n · k), because we store every word in the hash map."""  
        anagram_groups = {}

        for word in strs:
            key = ''.join(sorted(word))
            anagram_groups.setdefault(key, []).append(word)
        
        return list(anagram_groups.values())