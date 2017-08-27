#coding: utf-8
from math import sqrt, acos, pi
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
    NO_UNIQUE_PARALLEL_COMPONENT_MSG = 'No unique parallel component'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.index = 0
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def plus(self, v):
        new_coordinates = [x+y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        new_coordinates = [Decimal(c)*x for x in self.coordinates]
        return Vector(new_coordinates)

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    def normalized(self):
        """
        标准化向量
        :return:
        """
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal(1.0)/Decimal(magnitude))
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def dot(self, v):
        return sum([x * y for x, y in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()

            value = u1.dot(u2)

            # 此处是为了解决精度问题
            if value > 1.0:
                value = 1.0
            elif value < -1.0:
                value = -1.0
            elif abs(abs(value) - Decimal(1.0)) < 1e-10:
                if value < 0:
                    value = -1.0
                else:
                    value = 1.0
            angle_in_radians = acos(value)

            if in_degrees:
                degrees_per_radian = 180. / pi
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
            else:
                raise e

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def is_parallel_to(self, v):
        return (self.is_zero() or v.is_zero() or abs(self.angle_with(v)) <= 1e-10 or self.angle_with(v) == pi)

    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

    def component_parallel_to(self, basis):
        """
        向量投影的水平向量
        :param basis:
        :return:
        """
        try:
            u = basis.normalized()
            weigth = self.dot(u)
            return u.times_scalar(weigth)
        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e

    def component_orthogonal_to(self, basis):
        """
        向量投影的正交向量
        :param basis:
        :return:
        """
        try:
            projection = self.component_parallel_to(basis)
            return self.minus(projection)
        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e

    def cross(self, v):
        try:
            x_1, y_1, z_1 = self.coordinates
            x_2, y_2, z_2 = v.coordinates
            new_coordinates = [y_1 * z_2 - y_2 * z_1, -(x_1 * z_2 - x_2 * z_1), x_1 * y_2 - x_2 * y_1]
            return Vector(new_coordinates)
        except ValueError as e:
            msg = str(e)
            raise e

    def __iter__(self):
        # 在遍历前,将index重置为0
        self.index = 0
        return self

    def next(self):
        if self.index >= len(self.coordinates):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.coordinates[index]

    def __getitem__(self, item):
        return self.coordinates[item]

    def __setitem__(self, key, value):
        self.coordinates[key] = value

    def __index__(self, i):
        return i