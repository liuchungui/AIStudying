#coding: utf-8
from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from hyperPlane import HyperPlane
from parametrization import Parametrization

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
                indices[i] = p.first_nonzero_index(p.normal_vector)
            except Exception as e:
                if str(e) == HyperPlane.NO_NONZERO_ELTS_FOUND_MSG:
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
            c = self.planes[i].normal_vector[col]
            if not MyDecimal(c).is_near_zero():
                self.swap_rows(row, i)
                return True
        return False

    def clear_row(self, row, col):
        # print row, col
        num_equations = len(self.planes)
        beta = self.planes[row].normal_vector[col]
        # print beta
        for i in range(row+1, num_equations):
            c = self.planes[i].normal_vector[col]
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
                c = system.planes[i].normal_vector[j]
                if MyDecimal(c).is_near_zero():
                    swap_successed = system.swap_able(i, j)
                    if not swap_successed:
                        j += 1
                        continue
                system.clear_row(i, j)
                j += 1
                break
        return system

    def clear_first_var_rows(self, row, col):
        for i in range(row):
            c = self.planes[i].normal_vector[col]
            self.add_multiple_times_row_to_row(-c, row, i)

    def compute_rref(self):
        system = self.compute_triangular_form()

        num_equations = len(system.planes)
        num_var = system.dimension

        #从后往前
        i = num_equations - 1
        while i >= 0:
            #找到第一个首选变量
            p = system.planes[i]
            first_index = -1
            for k, item in enumerate(p.normal_vector):
                if not MyDecimal(item).is_near_zero():
                    first_index = k
                    break
            if first_index == -1:
                i -= 1
                continue

            #将此等式首选变量变成1
            c = system.planes[i].normal_vector[first_index]
            system.multiply_coefficient_and_row(MyDecimal(1.0)/c, i)

            #清空其它等式中的首选变量
            system.clear_first_var_rows(i, first_index)

            i -= 1

        return system

    def raise_exception_if_contradictory_equation(self):
        """
        检查有冲突的等式,其实就是检查是否存在0=1的等式
        :return:
        """
        for i,p in enumerate(self.planes):
            try:
                index = p.first_nonzero_index(p.normal_vector)
            except Exception as e:
                if str(e) == HyperPlane.NO_NONZERO_ELTS_FOUND_MSG:
                    #没有找到主变量,则检查该项是否存在 0 = 1的等式
                    if not MyDecimal(p.constant_term).is_near_zero():
                        raise Exception("存在冲突的等式")
                    else:
                        continue
                else:
                    raise e


    def extract_direction_vectors_for_parametrization(self):
        #变量数量
        num_var = self.dimension
        #主变量集合
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        #计算出自由变量的集合
        free_var_set = set(range(num_var)) - set(pivot_indices)

        direction_vectors = []

        #遍历自由变量,求出对应的方向向量
        for free_var in free_var_set:
            free_coords = [0] * num_var
            # 此处设置为1,是因为自由变量和自由变量相等,例如z=z
            free_coords[free_var] = 1
            for i, p in enumerate(self.planes):
                pivot_var = pivot_indices[i]
                #如果这个等式没有主变量,则直接跳出循环
                if pivot_var < 0:
                    break
                #此处用负号,是因为将等式移动到右边来,就变成负号了
                free_coords[pivot_var] = -p.normal_vector[free_var]
            direction_vectors.append(Vector(free_coords))

        return direction_vectors

    def extract_base_point_for_parametrization(self):
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        num_var = self.dimension

        base_point_array = [0] * num_var

        for i, item in enumerate(self.planes):
            pivot_var = pivot_indices[i]
            if pivot_var < 0:
                break
            base_point_array[pivot_var] = item.constant_term

        return Vector(base_point_array)

    def do_gaussian_elimination_and_parametrize_solution(self):
        #计算rref的解
        rref = self.compute_rref()

        #检查冲突等式
        rref.raise_exception_if_contradictory_equation()

        #方向向量
        direction_vectors = rref.extract_direction_vectors_for_parametrization()

        #basePoint 向量
        base_point_vector = rref.extract_base_point_for_parametrization()

        return Parametrization(base_point_vector, direction_vectors)


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps