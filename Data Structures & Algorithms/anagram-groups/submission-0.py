class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_groups = {}

        for word in strs:
            key = ''.join(sorted(word))
            anagram_groups.setdefault(key, []).append(word)
        
        return list(anagram_groups.values())