n = 12

l1 = []

def is_prime(n):
  for i in range(2,n//2+1):
    if n%i == 0:
      l1.append(i)
  if len(l1) == 0:
    return -1
  return l1
print(is_prime(n))hbvjhv
  