def print_divisible_numbers(start, end, num1, num2):
  l1 = []
  for i in range(start,end+1):
    if(i%num1 ==0 and i%num2==0):
      l1.append(i)
  print(l1)

print_divisible_numbers(10,50,3,5)
