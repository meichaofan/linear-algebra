from playLA.Vector import Vector
from playLA.GramSchmidtProcess import gram_schmidt_process

if __name__ == "__main__":
    basis1 = [Vector([2, 1]), Vector([1, 1])]
    res1 = gram_schmidt_process(basis1)
    for row in res1:
        print(row)

    res1 = [row / row.norm() for row in res1]
    for row in res1:
        print(row)
    print(res1[0].dot(res1[1]))
    print()

    basis4 = [Vector([1, 1, 5, 2]), Vector([-3, 3, 4, -2]), Vector([-1, -2, 2, 5])]
    res4 = gram_schmidt_process(basis4)
    res4 = [row / row.norm() for row in res4]
    for row in res4:
        print(row)
    print(res4[0].dot(res4[1]))
    print(res4[0].dot(res4[2]))
    print(res4[1].dot(res4[2]))
    print()
