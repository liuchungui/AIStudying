#coding=utf-8
from decimal import Decimal, getcontext

from vector import Vector

getcontext().prec = 30


class Plane(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 3

        if not normal_vector:
            all_zeros = [0]*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = 0.0
        self.constant_term = constant_term

        self.set_basepoint()


    def set_basepoint(self):
        try:
            n = self.normal_vector.coordinates
            c = self.constant_term
            basepoint_coords = [0]*self.dimension

            initial_index = Plane.first_nonzero_index(n)
            # print initial_index
            initial_coefficient = n[initial_index]
            # print '值'
            # print initial_coefficient
            # print type(initial_coefficient)
            # print c
            # print type(c)

            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e

    def is_parallel(self, other):
        #判断法向量平行就可以判断两个直线平行
        return self.normal_vector.parallel(other.normal_vector)

    def __eq__(self, other):
        print self.normal_vector, other.normal_vector
        if self.normal_vector == other.normal_vector and self.constant_term == other.constant_term:
            return True

        # 不平行,则不相等
        if self.is_parallel(other) == False:
            return False

        print self.basepoint, other.basepoint
        # 平行,找出两条线之间基点连接的向量
        v = self.basepoint - other.basepoint
        # 连接的向量与直线法向量正交,则相等
        if self.normal_vector.orthogonality(v):
            return True

        return False

    def is_equal(self, other):
        # 不平行,则不相等
        if self.is_parallel(other) == False:
            return False

        # 平行,找出两条线之间基点连接的向量
        v = self.basepoint - other.basepoint
        # 连接的向量与直线法向量正交,则相等
        if self.normal_vector.orthogonality(v):
            return True

        return False

    def __mul__(self, other):
        normal_vector = self.normal_vector * other
        constant_term = self.constant_term * other
        return Plane(normal_vector, constant_term)

    def __add__(self, other):
        normal_vector = self.normal_vector + other.normal_vector
        constant_term = self.constant_term + other.constant_term
        return Plane(normal_vector, constant_term)

    def intersection(self, other):
        """
        相交,则返回交点
        :param other:
        :return:
        """
        if self.is_equal(other):
            print '两条直线相等,交点就是两条直线'
        elif self.is_parallel(other):
            print '两条直线平行,没有交点'
        else:
            # ad - bc
            value = self.normal_vector.coordinates[0] * other.normal_vector.coordinates[1] - self.normal_vector.coordinates[1] * other.normal_vector.coordinates[0]
            x = (other.normal_vector.coordinates[1] * self.constant_term - self.normal_vector.coordinates[1] * other.constant_term) / value
            y = -(other.normal_vector.coordinates[0] * self.constant_term - self.normal_vector.coordinates[0] * other.constant_term) / value
            print (x, y)


    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector.coordinates

        try:
            # print self.dimension
            initial_index = Plane.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output


    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                # print '查找到'
                # print k
                return k
        raise Exception(Plane.NO_NONZERO_ELTS_FOUND_MSG)


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps