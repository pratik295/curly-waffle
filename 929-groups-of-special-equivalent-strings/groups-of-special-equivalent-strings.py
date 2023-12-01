class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        
        def norm(word):
            even=''.join(word[::2])
            odd=''.join(word[1::2])
            return ''.join(sorted(even))+''.join(sorted(odd))
        
        unique=set()

        
        for word in words:
            normal=norm(word)

            unique.add(normal)
        return len(unique)