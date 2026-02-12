"""
2062. Count Vowel Substrings of a String
link: https://leetcode.com/problems/count-vowel-substrings-of-a-string/
not clear(hehehe)
"""
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        count=0
        vowels=['a','e','i','o','u']
        for i in range (0, len(word)):
            if word[i] not in vowels:
                continue
            else:
                seen_a = seen_e = seen_i = seen_o = seen_u = False
            for j in range(i, len(word)):
                if word[j] not in vowels:
                    break
                if word[j] == 'a': seen_a = True
                if word[j] == 'e': seen_e = True
                if word[j] == 'i': seen_i = True
                if word[j] == 'o': seen_o = True
                if word[j] == 'u': seen_u = True
                if seen_a and seen_e and seen_i and seen_o and seen_u:
                    count += 1
        return count

