s = 'abcac'
n = 10

a_count = s.count('a')

actaul = n//len(s)

rem = n % 5
res = a_count*actaul
print(res)
if(rem != 0):
  res +=s[:rem].count('a')


print(res)