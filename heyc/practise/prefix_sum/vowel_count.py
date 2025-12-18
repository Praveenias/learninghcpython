s = "eleetminicoworoep"

prefix_sum = {}
vowel = ['a','e','i','o','u']
v_count = 0
for i in range(len(s)):
  if s[i] in vowel:
    v_count +=1

  prefix_sum[i] = v_count

print(prefix_sum)
