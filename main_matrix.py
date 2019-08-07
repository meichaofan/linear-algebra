from playLA.Matrix import Matrix
from playLA.Vector import Vector

if __name__ == "__main__":
    matrix = Matrix([[1, 2], [3, 4]])
    print(matrix)
    print("{} shape = {}".format(matrix, matrix.shape()))
    print("{} size = {}".format(matrix, matrix.size()))
    print("len(matrix({})) = {}".format(matrix, len(matrix)))
    print("matrix[0][0]  = {}".format(matrix[0, 0]))

    matrix2 = Matrix([[5, 6], [7, 8]])
    print("add {} + {} = {}".format(matrix, matrix2, matrix + matrix2))
    print("sub {} - {} = {}".format(matrix, matrix2, matrix - matrix2))

    print("zero 2 3 : {}".format(Matrix.zero(2, 3)))

    T = Matrix([[1.5, 0], [0, 2]])
    p = Vector([5, 3])
    print(T.dot(p))

    P = Matrix([[0, 4, 5], [0, 0, 3]])
    print(T.dot(P))
