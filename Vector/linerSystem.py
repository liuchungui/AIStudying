#coding:utf-8
from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane

getcontext().prec = 30


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def swap_rows(self, row1, row2):
        tmp = self.planes[row1]
        self.planes[row1] = self.planes[row2]
        self.planes[row2] = tmp


    def multiply_coefficient_and_row(self, coefficient, row):
        self.planes[row] = self.planes[row] * coefficient


    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        self.planes[row_to_be_added_to] = self.planes[row_to_be_added_to] + self.planes[row_to_add] * coefficient
        return self


    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector.coordinates)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices


    def __len__(self):
        return len(self.planes)


    def __getitem__(self, i):
        return self.planes[i]


    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret

    def swap_able(self, row, col):
        num_equations = len(self.planes)
        for i in range(row+1, num_equations):
            c = self.planes[i].normal_vector.coordinates[col]
            if not MyDecimal(c).is_near_zero():
                self.swap_rows(row, i)
                return True
        return False

    def clear_row(self, row, col):
        # print row, col
        num_equations = len(self.planes)
        beta = self.planes[row].normal_vector.coordinates[col]
        # print beta
        for i in range(row+1, num_equations):
            c = self.planes[i].normal_vector.coordinates[col]
            scale = - c / beta
            self.add_multiple_times_row_to_row(scale, row, i)

    def compute_triangular_form(self):
        system = deepcopy(self)
        # 等式数量
        num_equations = len(self.planes)
        # 变量数量
        num_var = system.dimension
        j = 0
        for i in range(num_equations):
            while j < num_var:
                c = system.planes[i].normal_vector.coordinates[j]
                if MyDecimal(c).is_near_zero():
                    swap_successed = system.swap_able(i, j)
                    if not swap_successed:
                        j += 1
                        continue
                system.clear_row(i, j)
                j += 1
                break
        return system


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps