class Solution:
    def solve(self, n, word):
      vowels = "aeiou"
    
      syllables = []
      i = 0
      while i < n:
          if i + 1 < n and word[i] not in vowels and word[i + 1] in vowels:
              syllables.append(word[i:i + 2])
              i += 2
          if (i + 2) < n and (word[i] not in vowels) and (word[i + 1] in vowels) and (word[i + 2] not in vowels):
              syllables.append(word[i:i + 3])
              i += 3
      return " ".join(syllables)
    
if __name__ == '__main__':
    s = Solution()
    print(s.solve(5,"badef"))