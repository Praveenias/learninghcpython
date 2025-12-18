n = 123

def add(a):
  if a < 10:
    return a
  return a%10 + add(a//10)

print(add(2126))

