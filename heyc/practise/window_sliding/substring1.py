s = "fororfrdofr"
t = "LAVA"

from collections import Counter
frquency = Counter(t)
required_len = len(frquency)
right,left = 0,0
formed = 0
min_start=0
min_len = float('inf')
window_frequency = {}
while right < len(s):
  char = s[right]
  window_frequency[char] = window_frequency.get(char,0)+1
  if char in window_frequency and window_frequency[char] == frquency[char]:
    formed +=1
  print(formed,char,frquency)
  while formed == required_len:
    
    if right-left +1 < min_len:
      min_len = right-left +1
      min_start = left
    left_char = s[left]
    window_frequency[left_char] -=1
   
    if left_char in window_frequency and window_frequency[left_char] < frquency[left_char]:
      formed -=1
    left +=1
  right +=1
print(min_len)
print(s[min_start:min_start+min_len])

