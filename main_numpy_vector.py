import numpy as np

if __name__ == "__main__":
    print(np.__version__)

    # np.array的创建
    vec = np.array([1, 2, 3])
    print(vec)

    # 零向量
    print(np.zeros(5))

    print(np.ones(5))
    print(np.full(5, 6))

    # np.array的基本属性
    vec = np.array([1, 2, 3])
    print("size = ", vec.size)
    print("size = ", len(vec))
    print(vec[0])
    print(vec[-1])
    print(vec[0:2])
    print(type(vec[0:2]))

    # np.array的基本运算
    vec2 = np.array([4, 5, 6])
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))
    print("{} * {} = {}".format(2, vec, 2 * vec))
    # 逐个元素相乘 ， 结果是一个向量（没有数学意义）
    print("{} * {} = {}".format(vec, vec2, vec * vec2))
    # 点乘，最后结果是标量
    print("{}.dot({}) = {}".format(vec, vec2, vec.dot(vec2)))

    # 模
    print(np.linalg.norm(vec))
    # 单位向量
    print(vec / np.linalg.norm(vec))
    print(np.linalg.norm(vec / np.linalg.norm(vec)))
