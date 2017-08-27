#coding: utf-8

from vector import Vector
import math

# test 1
v1 = Vector(['8.218', -9.341])
v2 = Vector([-1.129, 2.111])

print v1.plus(v2)

# test 2
v1 = Vector([7.119, 8.215])
v2 = Vector([-8.223, 0.878])
print v1.minus(v2)

# test 3
v1 = Vector([1.671, -1.012, -0.318])
print v1.times_scalar(7.41)

# 计算长度
v1 = Vector([-0.221, 7.437])
print v1.magnitude()
# unit_v1 = v1.unit()
# print unit_v1
# print unit_v1.len()

v2 = Vector([8.813, -1.331, -6.247])
print v2.magnitude()

v3 = Vector([5.581, -2.136])
print v3.magnitude()

v4 = Vector([1.996, 3.108, -4.554])
print v4.normalized()

# 编写点积和夹角函数
v1 = Vector([7.887, 4.138])
v2 = Vector([-8.802, 6.776])
print v1.dot(v2)

v1 = Vector([-5.955, -4.904, -1.874])
v2 = Vector([-4.496, -8.755, 7.103])
print v1.dot(v2)

v1 = Vector([3.183, -7.627])
v2 = Vector([-2.668, 5.319])
print v1.angle_with(v2)

v1 = Vector([7.35, 0.221, 5.188])
v2 = Vector([2.751, 8.259, 3.985])
angle = v1.angle_with(v2, True)
print angle

v1 = Vector([-7.579, -7.88])
v2 = Vector([22.737, 23.64])
print v1.is_parallel_to(v2)
print v1.is_orthogonal_to(v2)

v1 = Vector([-2.029, 9.97, 4.172])
v2 = Vector([-9.231, -6.639, -7.245])
print v1.is_parallel_to(v2)
print v1.is_orthogonal_to(v2)

v1 = Vector([-2.328, -7.284, -1.214])
v2 = Vector([-1.821, 1.072, -2.94])
print v1.is_parallel_to(v2)
print v1.is_orthogonal_to(v2)

v1 = Vector([2.118, 4.827])
v2 = Vector([0, 0])
print v1.is_parallel_to(v2)
print v1.is_orthogonal_to(v2)

# 向量投影
print("##########向量投影#######")
v1 = Vector([3.039, 1.879])
v2 = Vector([0.825, 2.036])
print v1.component_parallel_to(v2)

v1 = Vector([-9.88, -3.264, -8.159])
v2 = Vector([-2.155, -9.353, -9.473])
print v1.component_orthogonal_to(v2)

v1 = Vector([3.009, -6.172, 3.692, -2.51])
v2 = Vector([6.404, -9.144, 2.759, 8.718])
print v1.component_parallel_to(v2)
print v1.component_orthogonal_to(v2)

# 向量乘积
print("#########向量乘积#########")
v1 = Vector([8.462, 7.893, -8.187])
v2 = Vector([6.984, -5.975, 4.778])
print v1.cross(v2)

v1 = Vector([-8.987, -9.838, 5.031])
v2 = Vector([-4.268, -1.861, -8.866])
v3 = v1.cross(v2)
print v3.magnitude()

v1 = Vector([1.5, 9.547, 3.691])
v2 = Vector([-6.007, 0.124, 5.772])
v3 = v1.cross(v2)
print 0.5 * v3.magnitude()
print v1

for index, value in enumerate(v1):
    print index, value

# 交点
print("###########交点##########")