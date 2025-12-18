def power(a,n):
  if n == 1:
    return a
  return a * power(a,n-1)

print(power(2,3))
