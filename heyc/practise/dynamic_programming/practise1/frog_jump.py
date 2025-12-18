def frogJump(n: int, heights) -> int:
    def traverse(index):
        if index == n-1:
            return 0
    
        min1 = float('inf')
        min2 = float('inf')
        
        if index + 1 < n:
            min1 = traverse(index + 1) + abs(heights[index] - heights[index + 1])
        if index + 2 < n:
            min2 = traverse(index + 2) + abs(heights[index] - heights[index + 2])
        
        return min(min1, min2)
    return traverse(0)
print(frogJump(3,[10 ,20 ,30,10]))