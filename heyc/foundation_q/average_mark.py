class Solution:
    @staticmethod
    def calculate_average(name, M, S, E, H, C):
      print(name)
      print(round(sum([M,S,E,H,C])/5))

if __name__ == '__main__':
   Solution.calculate_average('A',81, 81, 81, 33, 63)