l1 = [1,2,3,4,5]
is_clockwise = False
rotate_n = -1

def rotate(l1:list,direc:bool,rotate_n:int) ->list:
  rotate_n = rotate_n%len(l1) 
  if direc:
    rotate_n *= -1
  return l1[rotate_n:]+l1[:rotate_n]

otp = rotate(l1,is_clockwise,rotate_n)
print(otp)
    