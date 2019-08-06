from playLA.Matrix import Matrix

if __name__ == "__main__":
    matrix = Matrix([[1, 2], [3, 4]])
    print(matrix)
    print("{} shape = {}".format(matrix, matrix.shape()))
    print("{} size = {}".format(matrix, matrix.size()))
    print("len(matrix({})) = {}".format(matrix, len(matrix)))
    print("matrix[0][0]  = {}".format(matrix[0, 0]))
