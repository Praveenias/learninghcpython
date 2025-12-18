start=5
end=20
divisor = 3

if start%divisor != 0:
  start = start + (divisor - start%divisor)
count = 0
for i in range(start,end+1,divisor):
  count +=1
print(count)