with open("sample.txt","r") as fout:
  for line in fout:
    print(line)


with open("sample.txt","w+") as f:
  f.write("Line1")
  print(f)