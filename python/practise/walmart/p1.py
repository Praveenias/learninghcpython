'''You are provided with a string ‘s’. Your task is to reverse the string using stack Data Structure.

 


Input Description:
You are given a string ‘s’.

Output Description:
Print the reverse string

Sample Input :
i am jsb
Sample Output :
jsb am i'''

ip = 'i am jsb'
s = []
for i in ip.split():
  s.append(i)
print(*s[::-1])