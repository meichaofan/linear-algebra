import matplotlib.pyplot as plt
from playLA.Matrix import Matrix
from playLA.Vector import Vector

if __name__ == "__main__":
    points = [[0, 0], [0, 5], [3, 5], [3, 4], [1, 4], [1, 3], [2, 3], [2, 2], [1, 2], [1, 0]]
    x = [e[0] for e in points]
    y = [e[1] for e in points]
    plt.figure(figsize=(5, 5))
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.plot(x, y)
    # plt.show()

    P = Matrix(points)
    # print(P.shape())
    # T = Matrix([[2, 0], [0, 1.5]])

    T = Matrix([[1, 0], [0, -1]])

    P2 = T.dot(P.T())
    # plt.plot(P2.row_vector(0), P2.row_vector(1))
    plt.plot([P2.col_vector(i)[0] for i in range(P2.col_num())],
             [P2.col_vector(i)[1] for i in range(P2.col_num())])
    plt.show()
