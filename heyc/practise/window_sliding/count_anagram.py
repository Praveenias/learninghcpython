from collections import Counter
s = "fororofrdofr"
word = "foro"

word_fre = Counter(word)
window_frequency = Counter(s[:len(word)-1])
anagram = 0

for i in range(len(word)-1,len(s)):
  #print(window_frequency)
  window_frequency[s[i]] +=1
  if window_frequency == word_fre:
    anagram +=1
  
  left_char = s[i-len(word) + 1]
  window_frequency[left_char] -=1
  if window_frequency[left_char] == 0:
    del window_frequency[left_char]
print(anagram)
