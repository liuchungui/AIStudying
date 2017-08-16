#coding=utf-8

import vector
import line

print "##########交点#########"
v1 = vector.Vector([4.046, 2.836])
l1 = line.Line(v1, 1.21)
v2 = vector.Vector([10.115, 7.09])
l2 = line.Line(v2, 3.025)
print l1.is_parallel(l2)
print l1.is_equal(l2)
l1.intersection(l2)

v1 = vector.Vector([7.204, 3.182])
l1 = line.Line(v1, 8.68)
v2 = vector.Vector([8.172, 4.114])
l2 = line.Line(v2, 9.883)
print l1.is_parallel(l2)
print l1.is_equal(l2)
l1.intersection(l2)

v1 = vector.Vector([1.182, 5.562])
l1 = line.Line(v1, 6.744)
v2 = vector.Vector([1.773, 8.343])
l2 = line.Line(v2, 9.525)
print l1.is_parallel(l2)
print l1.is_equal(l2)
l1.intersection(l2)