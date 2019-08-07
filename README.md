# linear-algebra
线性代数

### 向量的高级话题

#### 规范化和单位向量

1. 向量
2. 向量的模（长度）
3. 单位向量 （unit Vector）
4. 标准单位向量

#### 向量的点乘与几何意义

1. 两个向量“相乘”，结果是一个数！（标量）
2. 两个向量相乘，更严格的说法：两个向量的点乘，或两个向量的内积
3. 向量点乘的应用
   - 判断两个向量的夹角。
      - 如果点乘结果 = 0 ,两个向量垂直
      - 如果点乘结果 > 0 ,两个向量夹角为锐角
      - 如果点乘结果 < 0 ,两个向量夹角为钝角
   - 判断两个向量的相似程度（推荐系统）
   - 几何计算中，求投影点的坐标

### 矩阵 Matrix

#### 矩阵的基本运算

1. A + B = B + A
2. (A + B) + C = A + (B + C)
3. (ck)A = c(kA)
4. (c+k)A = cA+kA
5. k(A+B) = kA + kB
6. 存在矩阵O,满足：A + O = A
7. 存在矩阵-A,满足：A +（-A）= 0 ，且 -A 唯一

#### 把矩阵看做一个系统

1. 矩阵（系统系数）和向量相乘 A a = b
   - 矩阵A的列数必须和向量a的元素个数相等
   - 矩阵A的行数没有限制
   - 矩阵A实际上将向量a转换成了向量b
   - 可以把矩阵理解成向量的函数
2. 矩阵乘法 A * B = C 
    - 矩阵A的列数和矩阵B的行数相等
    - A是m * k的矩阵，B是k * n的矩阵，则结果矩阵是m * n的矩阵
    - 矩阵乘法不遵守交换律，很有可能交换后，不能相乘，即使能相乘，结果也不一样



