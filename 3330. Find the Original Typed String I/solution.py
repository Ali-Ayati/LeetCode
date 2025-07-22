class Solution:
    def possibleStringCount(self, word: str) -> int:
        
        group = []
        i = 0
        while i < len(word):
            count = 1
            
            while i + 1 < len(word) and word[i] == word[i+1]:
                count += 1
                i += 1
            
            group.append(count)
            i += 1
            
        result = 1
        
        for count in group:
            if count > 1:
                result += count - 1
        
        return result
    


a = "abbcccc"

solu = Solution()

print(solu.possibleStringCount(word=a))