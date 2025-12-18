height = [1,1]

i = 0
j = len(height)-1

max = 0
while i < j:
  min_height = min(height[i],height[j])
  c_max = (j-i)*min_height
  if c_max > max:
    max = c_max
  #print(min_height,(j-i)*min_height,max)
  if min_height == height[i]:
    i +=1
  else:
    j -=1
print(max)