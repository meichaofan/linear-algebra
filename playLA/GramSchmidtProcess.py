from .Matrix import Matrix
from .LinearSystem import rank

"""格林姆-施密特正交基过程"""


def gram_schmidt_process(basis):
    matrix = Matrix(basis)
    # 向量组线性无关
    assert rank(matrix) == len(basis)

    res = [basis[0]]
    for i in range(1, len(basis)):
        p = basis[i]
        for r in res:
            p = p - basis[i].dot(r) / r.dot(r) * r
        res.append(p)
    return res
