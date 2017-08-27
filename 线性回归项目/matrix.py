#coding: utf-8
import sys

class Matrix(object):
    """
    矩阵类
    """
    def __init__(self, data):
        """
        初始化矩阵
        :param data:
        """
        self.data = data
        self.rows = len(data)

        #列的数量
        for i in range(self.rows):
            if i == 0:
                self.cols = len(data[i])
            elif self.cols != len(data[i]):
                raise Exception('因为数组中元素数量不一致,列的数量无法获知')

    def __str__(self):
        out_put = ""
        for i in range(self.rows):
            if i != 0:
                out_put += " "
            out_put += "["
            for j in range(self.cols):
                if j == 0:
                    out_put += str(self.data[i][j])
                else:
                    out_put += ', ' + str(self.data[i][j])
            out_put += "]"
            if i != self.rows - 1:
                out_put += "\n"
        return "[" + out_put + "]"

    def shape(self):
        return self.rows, self.cols

    def round(self, decPts=4):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = round(self.data[i][j], decPts)

    def transpose(self):
        result = [[0 for x in range(self.rows)] for x in range(self.cols)]
        for i in range(self.rows):
            for j in range(self.cols):
                result[j][i] = self.data[i][j]
        return Matrix(result)

    def __mul__(self, other):
        """
        矩阵相乘
        :param other:
        :return:
        """
        if self.cols != other.rows:
            return None
        result = [[0 for x in range(other.cols)] for x in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                for k in range(other.cols):
                    result[i][k] += self.data[i][j] * other.data[j][k]

        return Matrix(result)

    def augmentMatrix(self, other):
        if self.rows != other.rows:
            return None
        result = [[0 for x in range(self.cols + other.cols)] for x in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self.data[i][j]
            for k in range(other.cols):
                result[i][self.cols+k] = other.data[i][k]
        return Matrix(result)

    def swapRows(self, r1, r2):
        if r1 == r2:
            return
        tmp = 0
        for i in range(self.cols):
            tmp = self.data[r1][i]
            self.data[r1][i] = self.data[r2][i]
            self.data[r2][i] = tmp
        return

    def scaleRow(self, r, scale):
        # 注意,当scale为0时,需要抛出错误
        if scale == 0:
            raise ValueError
        if r >= self.rows or r < 0:
            return
        for i in range(self.cols):
            self.data[r][i] *= scale



    # TODO r1 <--- r1 + r2*scale
    # 直接修改参数矩阵，无返回值
    def addScaledRow(self, r1, r2, scale):
        for i in range(self.cols):
            self.data[r1][i] += self.data[r2][i] * scale

    def gj_Solve(self, b, decPts=4, epsilon = 1.0e-16):
        """
        高斯消元
        :param b: 矩阵
        :param decPts: 四舍五入的位数
        :param epsilon: 判断为0的阈值
        :return:
        """
        if self.rows != b.rows:
            return None
        ab = self.augmentMatrix(b)
        max_value = 0
        max_row = -1
        for col in range(ab.cols-1):
            max_value = ab.data[col][col]
            max_row = col
            # print '遍历第{}列'.format(col)
            # print max_value, max_row
            for row in range(col+1, self.rows):
                if abs(ab.data[row][col]) > abs(max_value):
                    max_value = abs(ab.data[row][col])
                    max_row = row

            # 判断最大值是否为0
            if abs(max_value) <= epsilon:
                return None

            # 交换行
            if max_row != col:
                ab.swapRows(max_row, col)

            # 将列C的对角元素缩放为1
            ab.scaleRow(col, 1.0 / ab.data[col][col])

            # 将列C的其它元素消为0
            for row in range(ab.rows):
                if row == col:
                    continue
                # 主要这一步,将col列的其它行元素消除为0,很巧妙的保持以前列唯一元素仍然为1
                ab.addScaledRow(row, col, -ab.data[row][col]/ab.data[col][col])


        ab.round(decPts)

        return Matrix([[ab.data[row][ab.cols-1]] for row in range(ab.rows)]).data



    @staticmethod
    def unit(n):
        """
        创建一个n阶单位矩阵
        :param n:
        :return:
        """
        data_array = []

        for i in range(n):
            data_array.append([0] * n)

        for i in range(n):
            for j in range(n):
                if i == j:
                    data_array[i][j] = 1
                else:
                    data_array[i][j] = 0

        return Matrix(data=data_array)


if __name__ == '__main__':
    m = Matrix.unit(4)
    print m

    data = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]

    m = Matrix(data)
    print m
    print m.shape()

    print m.transpose()

    data1 = [
        [1, 2],
        [3, 4]
    ]
    data2 = [
        [5],
        [6]
    ]
    m1 = Matrix(data1)
    m2 = Matrix(data2)
    # print m1 * m2
    m3 = m1.augmentMatrix(m2)
    print m1
    print m2
    print m3

    m1.scaleRow(1, 6)
    print m1