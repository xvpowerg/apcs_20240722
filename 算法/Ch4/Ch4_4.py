def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j],end = " ")
        print()    
array = [[1,2,3],
         [4,5,6]]

#printMatrix(array)
matrixA = [[None] * 2 for row in range(3)]
for i in range(3):
    row = []
    for j in range(2):
        matrixA[i][j] = 2* (i+1) + (j+1)
        
printMatrix(matrixA)        
