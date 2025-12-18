def transpose(matrix):
        res = []
        for i in range(len(matrix[0])):
            temp = []
            for j in range(len(matrix)):
              temp.append(matrix[j][i])
            res.append(temp)
            
        print(res)

transpose([[1,2,3],[4,5,6]])