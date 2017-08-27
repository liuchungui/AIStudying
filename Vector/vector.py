#coding: utf-8
import math

class Vector():
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def __add__(self, other):
        result = []
        for i, value in enumerate(self.coordinates):
            result.append(value + other.coordinates[i])
        return Vector(result)

    def __mul__(self, other):
        result = []
        for value in self.coordinates:
            result.append(other * value)
        return Vector(result)

    def __sub__(self, other):
        result = []
        for i, value in enumerate(self.coordinates):
            result.append(value - other.coordinates[i])
        return Vector(result)

    def len(self):
        def x_pow(x):
            return x * x
        value = map(x_pow, self.coordinates)
        # 对value序列求和并开根号
        length = sum(value) ** 0.5
        return length

    def unit(self):
        length = self.len()

        def dive_value(x):
            return x / length

        list_array = map(dive_value, self.coordinates)
        # print list_array
        return Vector(list_array)

    def dot(self, other):
        result = []
        # print other.coordinates
        for i, value in enumerate(self.coordinates):
            result.append(other.coordinates[i] * self.coordinates[i])

        return sum(result)

    def angle(self, other, degree=False):
        # value = self.dot(other)
        # rad_value = math.acos(value/(self.len() * other.len()))
        u1 = self.unit()
        u2 = other.unit()
        value = u1.dot(u2)
        rad_value = math.acos(value)
        if degree:
            return rad_value * 180 / math.pi
        else:
            return rad_value

    def parallel(self, other):
        # 是否为平行向量
        # 零向量为任何向量的平行向量
        if self.len() == 0 or other.len() == 0:
            return True

        if self == other:
            return True

        scale = 0
        for i, value in enumerate(self.coordinates):
            if i == 0:
                if self.coordinates[i] == 0:
                    scale = self.coordinates = 0
                scale = other.coordinates[i] / self.coordinates[i]
            else:
                if self.coordinates[i] == 0:
                    if scale != 0:
                        return False
                elif scale != other.coordinates[i] / self.coordinates[i]:
                    return False
        return True

    def orthogonality(self, other):
        # 是否为正交向量
        if self.len() == 0 or other.len() == 0:
            return True

        value = self.dot(other)
        if (value >= 0 and value < 1e-6) or (value <= 0 and value > -1e-6):
            return True
        return False

    def parallel_vector(self, vb):
        # 求平行向量
        unit_vb = vb.unit()
        value = unit_vb * self.dot(unit_vb)
        # print value
        return value

    def orth_vector(self, vb):
        # 求v在b上的正交向量
        parallel_v = self.parallel_vector(vb)
        # print parallel_v
        orth_v = self - parallel_v
        # print orth_v
        return orth_v

    def multi(self, other):
        '''
        求两个向量的乘积
        :param other:
        :return:
        '''
        if len(self.coordinates) != 3 or len(other.coordinates) != 3:
            return False
        x = self.coordinates[1] * other.coordinates[2] - self.coordinates[2] * other.coordinates[1]
        y = -(self.coordinates[0] * other.coordinates[2] - self.coordinates[2] * other.coordinates[0])
        z = self.coordinates[0] * other.coordinates[1] - self.coordinates[1] * other.coordinates[0]

        return Vector([x, y, z])

    def __index__(self, i):
        return self.coordinates[i]