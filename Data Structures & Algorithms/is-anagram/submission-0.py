class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Time is O(n) — two linear passes, so O(2n), which simplifies to O(n). 
        Space is O(k), where k is the number of distinct characters.
        Since the input is limited to 26 lowercase English letters, k is bounded, so space is effectively O(1)."""
        
        if len(s) != len(t):
            return False

        char_count_s = dict()
        char_count_t = dict()

        for char in s:
            char_count_s[char] = char_count_s.get(char, 0) + 1
        for char in t:
            char_count_t[char] = char_count_t.get(char, 0) + 1
        if char_count_s == char_count_t:
            return True
        return char_count_s == char_count_t
        