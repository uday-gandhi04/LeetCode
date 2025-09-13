from collections import Counter

class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = set("aeiou")
        freq = Counter(s)   # count frequency of each character

        max_vowel = 0
        max_consonant = 0

        for ch, count in freq.items():
            if ch in vowels:
                max_vowel = max(max_vowel, count)
            else:
                max_consonant = max(max_consonant, count)

        return max_vowel + max_consonant