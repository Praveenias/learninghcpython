s = "leetcode" 
k = 3

vowel_count = 0
s_count = 0
maxv = 0
left = 0
vowel = ['a','e','i','o','u']
for i in range(k):
  if s[i] in vowel:
    vowel_count +=1
maxv = vowel_count
print(maxv)
for i in range(k,len(s)):
  #print(s[i],s[i] in vowel,s[i-k])
  if s[i] in vowel:
   # print("hit")
    vowel_count +=1
  if s[i-k] in vowel:
    vowel_count -=1
  print(vowel_count,maxv)
  maxv = max(maxv,vowel_count)
  
  
print(maxv)

