from collections import deque
def firstNonRep(s):
  char_ferquency = {}
  res = []
  queue = deque()
  for i in range(len(s)):
    char_ferquency[s[i]] = char_ferquency.get(s[i],0)+1
    queue.append(s[i])

    while queue and char_ferquency[queue[0]] > 1:
      queue.popleft()

    res.append(queue[0] if queue else 'X')

  print(res)

firstNonRep("dabc")


