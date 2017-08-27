#coding: utf-8
from matrix import Matrix
import random

def shape(data):
    m = Matrix(data)
    return m.shape()

def matxRound(data, decPts=4):
    m = Matrix(data)
    m.round(decPts)
    print m

def transpose(data):
    m = Matrix(data)
    m = m.transpose()
    return m.data

def matxMultiply(data1, data2):
    m1 = Matrix(data1)
    m2 = Matrix(data2)
    m3 = m1 * m2
    return m3.data

def augmentMatrix(data1, data2):
    m1 = Matrix(data1)
    m2 = Matrix(data2)
    m3 = m1.augmentMatrix(m2)
    return m3.data

def swapRows(data, r1, r2):
    m = Matrix(data)
    m.swapRows(r1, r2)

def scaleRow(data, r, scale):
    m = Matrix(data)
    m.scaleRow(r, scale)

def addScaledRow(data, r1, r2, scale):
    m = Matrix(data)
    m.addScaledRow(r1, r2, scale)

def gj_Solve(A, b, decPts=4, epsilon=1.0e-16):
    """
    Gaussian Jordan 方法求解 Ax = b.
        参数
            A: 方阵
            b: 列向量
            decPts: 四舍五入位数，默认为4
            epsilon: 判读是否为0的阈值，默认 1.0e-16

        返回列向量 x 使得 Ax = b
        返回None，如果 A，b 高度不同
        返回None，如果 A 为奇异矩阵
    """
    m1 = Matrix(A)
    m2 = Matrix(b)
    retValue = m1.gj_Solve(m2, decPts=decPts, epsilon=epsilon)
    return retValue

def linearRegression(points):
    '''
    将3.1计算损失函数的证明结果用进来,从而化解成求二元一次方程的解
    参数：(x,y) 二元组列表
    返回：m，b
    '''
    a = 0
    b = 0
    c = 0
    d = 0
    k1 = 0
    k2 =0
    for point in points:
        a += 2 * point[0] * point[0]
        b += 2 * point[0]
        c += 2 * point[0]
        d += 2
        k1 += 2 * point[0] * point[1]
        k2 += 2 * point[1]

    # 求方程的解
    m = (d * k1 - b * k2) / (a * d - b * c)
    b = (-c * k1 + a * k2) / (a * d - b * c)
    return m, b

if __name__ == '__main__':
    a = [['a', 'b']]
    b = [['c']]

    # 构造线性方程
    def cal_y(x):
        return 7 * x - 2
    r = random.Random()
    l = [r.randint(0, 10000) for i in range(100)]
    l_list = []
    for x in l:
        l_list.append((x, cal_y(x)))
    print linearRegression(l_list)