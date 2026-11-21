class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        treq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1
        for cha in t:
            treq[cha]=treq.get(cha, 0)+1
        return freq == treq
        
        