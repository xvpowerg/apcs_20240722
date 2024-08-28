def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()
def flip(matrixA):
    matrixB = []
    r = len(matrixA)
    for i in range(r - 1,-1,-1):
        matrixB.append(matrixA[i])
    return matrixB

m1 = [[1,4],
      [2,5],
      [3,6]]
m2 = flip(m1)
printMatrix(m1)
print("=======")
printMatrix(m2)
