from ._global import is_zero, is_equal
import math


class Vector:

    def __init__(self, lst):
        # lst 复制，防止被外部修改
        self._values = list(lst)

    def norm(self):
        """返回向量的模"""
        return math.sqrt(sum(e ** 2 for e in self))

    def normalize(self):
        """返回向量的单位向量（规范化）"""
        if is_zero(self.norm()):
            raise ZeroDivisionError("Normalize error! norm is zero.")
        return Vector(self._values) / self.norm()

    def underlying_list(self):
        """返回向量低层列表"""
        return self._values[:]

    @classmethod
    def zero(cls, dim):
        """返回一个dim维的零向量"""
        return Vector([0] * dim)

    def __add__(self, other):
        """向量加法，返回结果向量"""
        assert len(self) == len(other), \
            "Error in adding. Length of vectors must be same."
        return Vector([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        """向量减法，返回结果向量"""
        assert len(self) == len(other), \
            "Error in adding. Length of vectors must be same."
        return Vector([a - b for a, b in zip(self, other)])

    def dot(self, other):
        """向量点乘，返回结果是标量"""
        assert len(self) == len(other), \
            "Error in adding. Length of vectors must be same."
        return sum(a * b for a, b in zip(self, other))

    def __mul__(self, k):
        """返回数量乘法的结果：self * k """
        return Vector([k * a for a in self])

    def __rmul__(self, k):
        """返回数量乘法的结果：k * self """
        return self * k

    def __truediv__(self, k):
        """返回数量除法的结果: self / k """
        return (1 / k) * self

    def __pos__(self):
        """返回向量取正的结果向量"""
        return 1 * self

    def __neg__(self):
        """返回向量取负的结果向量"""
        return -1 * self

    def __eq__(self, other):
        """判断两个向量是否相等"""
        other_list = other.underlying_list()
        if len(self._values) != len(other_list):
            return False
        return all([is_equal(x, y) for x, y in zip(self._values, other_list)])

    def __ne__(self, other):
        """判断两个向量是否不等"""
        return not (self == other)

    def __iter__(self):
        """返回向量的迭代器"""
        return self._values.__iter__()

    def __getitem__(self, index):
        """取向量的第index个元素"""
        return self._values[index]

    def __len__(self):
        """返回向量长度（有多少个元素）"""
        return len(self._values)

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))
