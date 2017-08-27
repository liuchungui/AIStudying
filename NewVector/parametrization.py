#coding: utf-8
from vector import Vector

class Parametrization(object):
    def __init__(self, base_point_vector, free_direction_vectors):
        self.base_point_vector = base_point_vector
        self.free_direction_vectors = free_direction_vectors

    def __str__(self):
        #判断自由变量数量是否多于1
        free_var_num = len(self.free_direction_vectors)
        out_put = ""
        for i, item in enumerate(self.base_point_vector):
            out_put += "{:.3f}".format(item)
            for j, direction_vector in enumerate(self.free_direction_vectors):
                value = direction_vector[i]
                #第i个等式如果的系数不为0,则显示出来
                if not abs(value) < 1e-10:
                    if value > 0:
                        out_put += " + {:.3f}t".format(value)
                    elif value < 0:
                        out_put += " - {:.3f}t".format(abs(value))
                    if free_var_num > 1:
                        out_put += "{:d}".format(j+1)
            out_put += "\n"
        return out_put
