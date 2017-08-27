#coding=utf-8
import plane
import vector

v1 = vector.Vector([-0.412, 3.806, 0.728])
p1 = plane.Plane(v1, -3.46)
v2 = vector.Vector([1.03, -9.515, -1.82])
p2 = plane.Plane(v2, 8.65)
print p1.is_parallel(p2)
print p1 == p2

v1 = vector.Vector([2.611, 5.528, 0.283])
p1 = plane.Plane(v1, 4.6)
v2 = vector.Vector([7.715, 8.306, 5.342])
p2 = plane.Plane(v2, 3.76)
print p1.is_parallel(p2)
print p1 == p2

v1 = vector.Vector([-7.926, 8.625, -7.212])
p1 = plane.Plane(v1, -7.952)
v2 = vector.Vector([-2.642, 2.875, -2.404])
p2 = plane.Plane(v2, -2.443)
print p1.is_parallel(p2)
print p1 == p2
