def calculate_and_display_property(land_values):
  def right_min():
    left_contribution = [0] * len(land_values)
    stack = []
    for i in range(len(land_values)):
        while stack and land_values[stack[-1]] < land_values[i]:
            stack.pop()
        if stack:
            left_contribution[i] = left_contribution[stack[-1]] + sum(land_values[stack[-1] + 1 : i])
        else:
            left_contribution[i] =0  # Everything to the left
        stack.append(i)
    return left_contribution
  def left_min():
    right = [0] * len(land_values)
    stack = []
    for i in range(len(land_values) - 1, -1, -1):
        while stack and land_values[stack[-1]] < land_values[i]:
            stack.pop()
        if stack:
            right[i] = right[stack[-1]] + sum(land_values[i + 1 : stack[-1]])
        else:
            right[i] = sum(land_values[i + 1 :])  # Everything to the right
        stack.append(i)
    return right
  
  left  = right_min()
  right = left_min()
  print(left,right)
  res = []
  for i,j in enumerate(land_values):
    res.append(j+left[i]+right[i])
  print(res)

calculate_and_display_property([4 ,3 ,5, 1, 2])