'''You are given a string of different type of brackets. Your task is to check 
whether the given string is balanced or not balanced.
A string is said to be balanced if the number of opening brackets are equal to 
the number of closing brackets where the brackets should be of same kind.


Input Description:
You are given a string ‘s’.

Output Description:
Print 'yes' if the given string is balanced and no if it is not

Sample Input :
{}(())[][][{}]
Sample Output :
yes'''


input = "()()()()("
input_config = {
  "]":"[",
  "}":"{",
  ")":"("
}

def check_symbols(input:str) -> str :
  stack = []
  for symbol in input:
    if symbol not in input_config:
      stack.append(symbol)
    if symbol in input_config:
      if len(stack) == 0:
        return "no"
      if input_config[symbol] != stack.pop() :
        return "no"
    
  return "yes" if len(stack) ==0 else 'no'

print(check_symbols(input))



  

