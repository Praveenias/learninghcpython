operations=["1","C"]
output = []
for data in operations:
    if data == "C":
      output = output[:-1]
    elif data == "D":
      output.append(output[-1]*2)
    elif data == "+":
      output.append(sum(output[-2:]))
    else:
      output.append(int(data))


print(sum(output))
        
        