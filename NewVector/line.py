#coding: utf-8
from decimal import Decimal, getcontext

from vector import Vector
from collections import Iterable

getcontext().prec = 30


class Line(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
            all_zeros = ['0']*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()


    def set_basepoint(self):
        try:
            n = self.normal_vector
            c = self.constant_term
            basepoint_coords = ['0']*self.dimension

            initial_index = Line.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e


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

        n = self.normal_vector

        try:
            initial_index = Line.first_nonzero_index(n)
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

    def is_parallel(self, other):
        #判断法向量平行就可以判断两个直线平行
        return self.normal_vector.is_parallel_to(other.normal_vector)

    def is_equal(self, other):
        # 不平行,则不相等
        if self.is_parallel(other) == False:
            return False

        # 平行,找出两条线之间基点连接的向量
        v = self.basepoint - other.basepoint
        # 连接的向量与直线法向量正交,则相等
        if self.normal_vector.is_orthogonal_to(v):
            return True

        return False

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
            value = self.normal_vector[0] * other.normal_vector[1] - self.normal_vector[1] * other.normal_vector[0]
            x = (other.normal_vector[1] * self.constant_term - self.normal_vector[1] * other.constant_term) / value
            y = -(other.normal_vector[0] * self.constant_term - self.normal_vector[0] * other.constant_term) / value
            print (x, y)



    @staticmethod
    def first_nonzero_index(iterable):
        # print isinstance(iterable, Iterable)
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps