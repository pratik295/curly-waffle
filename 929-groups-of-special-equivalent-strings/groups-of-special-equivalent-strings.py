from typing import List

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def normalize(word):
            even_chars = ''.join(word[::2])
            odd_chars = ''.join(word[1::2])
            return ''.join(sorted(even_chars)) + ''.join(sorted(odd_chars))

        unique_normalized_words = set()

        for word in words:
            normalized_word = normalize(word)
            unique_normalized_words.add(normalized_word)

        return len(unique_normalized_words)
