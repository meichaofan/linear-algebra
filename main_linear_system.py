from playLA.Matrix import Matrix
from playLA.Vector import Vector
from playLA.LinearSystem import LinearSystem
from playLA.LinearSystem import inv, rank

if __name__ == "__main__":
    A = Matrix([[1, 2, 4], [3, 7, 2], [2, 3, 3]])
    b = Vector([7, -11, 1])
    ls = LinearSystem(A, b)
    ls.gauss_jordan_elimination()
    ls.fancy_print()
    print()

    A2 = Matrix([[1, -3, 5], [2, -1, -3], [3, 1, 4]])
    b2 = Vector([-9, 19, -13])
    ls2 = LinearSystem(A2, b2)
    ls2.gauss_jordan_elimination()
    ls2.fancy_print()
    print()

    A3 = Matrix([[1, -1, 2, 0, 3],
                 [-1, 1, 0, 2, -5],
                 [1, -1, 4, 2, 4],
                 [-2, 2, -5, -1, -3]])
    b3 = Vector([1, 5, 13, -1])
    ls3 = LinearSystem(A3, b3)
    if not ls3.gauss_jordan_elimination():
        print("No solution")
    print("ls3")
    ls3.fancy_print()
    print()

    A4 = Matrix([[2, 2],
                 [2, 1],
                 [1, 2]])
    b4 = Vector([3, 2.5, 7])
    ls4 = LinearSystem(A4, b4)
    if not ls4.gauss_jordan_elimination():
        print("No solution")
    ls4.fancy_print()
    print()

    A5 = Matrix([[1, 2], [3, 4]])
    invA5 = inv(A5)
    print(invA5)
    print(A5.dot(invA5))
    print(invA5.dot(A5))

    print(rank(A3))
