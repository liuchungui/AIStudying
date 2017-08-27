#coding:utf-8
from plane import Plane
from vector import Vector
from linerSystem import LinearSystem, MyDecimal, Decimal

# p0 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p1 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
# p2 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
# p3 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
#
# s = LinearSystem([p0,p1,p2,p3])
#
# print '########start#########'
# print s.indices_of_first_nonzero_terms_in_each_row()
# print '{},{},{},{}'.format(s[0],s[1],s[2],s[3])
# print len(s)
# print s
#
# s[0] = p1
# print s
#
# print MyDecimal('1e-9').is_near_zero()
# print MyDecimal('1e-11').is_near_zero()

# p0 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p1 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
# p2 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
# p3 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
#
# s = LinearSystem([p0,p1,p2,p3])
# s.swap_rows(0,1)
#
# print "test case 1"
# if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
#     print 'test case 1 failed'
#
# print "test case 2"
# s.swap_rows(1,3)
# if not (s[0] == p1 and s[1] == p3 and s[2] == p2 and s[3] == p0):
#     print 'test case 2 failed'
#
# print "test case 3"
# s.swap_rows(3,1)
# if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
#     print 'test case 3 failed'
#
# print "test case 4"
# s.multiply_coefficient_and_row(1,0)
# if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
#     print 'test case 4 failed'
#
# print "test case 5"
# s.multiply_coefficient_and_row(-1,2)
# if not (s[0] == p1 and
#         s[1] == p0 and
#         s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
#         s[3] == p3):
#     print 'test case 5 failed'
#
# print "test case 6"
# s.multiply_coefficient_and_row(10,1)
# if not (s[0] == p1 and
#         s[1] == Plane(normal_vector=Vector(['10','10','10']), constant_term='10') and
#         s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
#         s[3] == p3):
#     print 'test case 6 failed'
#
# print "test case 7"
# s.add_multiple_times_row_to_row(0,0,1)
# if not (s[0] == p1 and
#         s[1] == Plane(normal_vector=Vector(['10','10','10']), constant_term='10') and
#         s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
#         s[3] == p3):
#     print 'test case 7 failed'
#
# print "test case 8"
# s.add_multiple_times_row_to_row(1,0,1)
# if not (s[0] == p1 and
#         s[1] == Plane(normal_vector=Vector(['10','11','10']), constant_term='12') and
#         s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
#         s[3] == p3):
#     print 'test case 8 failed'
#
# print "test case 9"
# s.add_multiple_times_row_to_row(-1,1,0)
# if not (s[0] == Plane(normal_vector=Vector(['-10','-10','-10']), constant_term='-10') and
#         s[1] == Plane(normal_vector=Vector(['10','11','10']), constant_term='12') and
#         s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
#         s[3] == p3):
#     print 'test case 9 failed'
#
# exit()

# print 'test case 1'
# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['0','1','1']), constant_term='2')
# s = LinearSystem([p1,p2])
# t = s.compute_triangular_form()
# if not (t[0] == p1 and
#         t[1] == p2):
#     print 'test case 1 failed'
#
# print 'test case 2'
# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1','1','1']), constant_term='2')
# s = LinearSystem([p1,p2])
# t = s.compute_triangular_form()
# if not (t[0] == p1 and
#         t[1] == Plane(constant_term='1')):
#     print 'test case 2 failed'
#
# print 'test case 3'
# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
# p4 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
# s = LinearSystem([p1,p2,p3,p4])
# t = s.compute_triangular_form()
# if not (t[0] == p1 and
#         t[1] == p2 and
#         t[2] == Plane(normal_vector=Vector(['0','0','-2']), constant_term='2') and
#         t[3] == Plane()):
#     print 'test case 3 failed'
#
# print 'test case 4'
# p1 = Plane(normal_vector=Vector(['0','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1','-1','1']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1','2','-5']), constant_term='3')
# s = LinearSystem([p1,p2,p3])
# t = s.compute_triangular_form()
# if not (t[0] == Plane(normal_vector=Vector(['1','-1','1']), constant_term='2') and
#         t[1] == Plane(normal_vector=Vector(['0','1','1']), constant_term='1') and
#         t[2] == Plane(normal_vector=Vector(['0','0','-9']), constant_term='-2')):
#     print 'test case 4 failed'



# print ("编写RREF函数")
# print "test case 1"
# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['0','1','1']), constant_term='2')
# s = LinearSystem([p1,p2])
# r = s.compute_rref()
# if not (r[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term='-1') and
#         r[1] == p2):
#     print 'test case 1 failed'
#
# print s
# print r
#
# print "test case 2"
# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1','1','1']), constant_term='2')
# s = LinearSystem([p1,p2])
# r = s.compute_rref()
# if not (r[0] == p1 and
#         r[1] == Plane(constant_term='1')):
#     print 'test case 2 failed'
# print s
# print r
#
# print "test case 3"
# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
# p4 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
# s = LinearSystem([p1,p2,p3,p4])
# r = s.compute_rref()
# if not (r[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term='0') and
#         r[1] == p2 and
#         r[2] == Plane(normal_vector=Vector(['0','0','-2']), constant_term='2') and
#         r[3] == Plane()):
#     print 'test case 3 failed'
# print s
# print r
#
# print "test case 4"
# p1 = Plane(normal_vector=Vector(['0','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1','-1','1']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1','2','-5']), constant_term='3')
# s = LinearSystem([p1,p2,p3])
# r = s.compute_rref()
# if not (r[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term=Decimal('23')/Decimal('9')) and
#         r[1] == Plane(normal_vector=Vector(['0','1','0']), constant_term=Decimal('7')/Decimal('9')) and
#         r[2] == Plane(normal_vector=Vector(['0','0','1']), constant_term=Decimal('2')/Decimal('9'))):
#     print 'test case 4 failed'
# print s
# print r
#
#
# # [::-1]是切片编程的一部分,就是将数组倒过来
# array = [1, 2, 3, 4, 5]
# print array[::-1]
#
# #编写高斯消除求解函数
# print "高斯消除求解函数"
#
# p1 = Plane(normal_vector=Vector([5.862, 1.178, -10.366]), constant_term=-8.15)
# p2 = Plane(normal_vector=Vector([-2.931, -0.589, 5.183]), constant_term=-4.075)
# s = LinearSystem([p1, p2])
# r = s.compute_rref()
# print r
#
# p1 = Plane(normal_vector=Vector([8.631, 5.112, -1.816]), constant_term=-5.113)
# p2 = Plane(normal_vector=Vector([4.315, 11.132, -5.27]), constant_term=-6.775)
# p3 = Plane(normal_vector=Vector([-2.158, 3.01, -1.727]), constant_term=-0.831)
# s = LinearSystem([p1, p2, p3])
# r = s.compute_rref()
# print r
#
# p1 = Plane(normal_vector=Vector([5.262, 2.739, -9.878]), constant_term=-3.441)
# p2 = Plane(normal_vector=Vector([5.111, 6.358, 7.638]), constant_term=-2.152)
# p3 = Plane(normal_vector=Vector([2.016, -9.924, -1.367]), constant_term=-9.278)
# p4 = Plane(normal_vector=Vector([2.167, -13.543, -18.883]), constant_term=-10.567)
# s = LinearSystem([p1, p2, p3])
# r = s.compute_rref()
# print r

print "编写参数化函数"
p1 = Plane(normal_vector=Vector([0.786, 0.786, 0.588]), constant_term=-0.714)
p2 = Plane(normal_vector=Vector([-0.138, -0.138, 0.244]), constant_term=0.319)
s = LinearSystem([p1, p2])
print s.compute_rref()
print s.do_gaussian_elimination_and_parametrize_solution()

p1 = Plane(normal_vector=Vector([8.631, 5.112, -1.816]), constant_term=-5.113)
p2 = Plane(normal_vector=Vector([4.315, 11.132, -5.27]), constant_term=-6.775)
p3 = Plane(normal_vector=Vector([-2.158, 3.01, -1.727]), constant_term=-0.831)
s = LinearSystem([p1, p2, p3])
# r = s.compute_rref()
# print r
print s.do_gaussian_elimination_and_parametrize_solution()


p1 = Plane(normal_vector=Vector([0.935, 1.76, -9.365]), constant_term=-9.955)
p2 = Plane(normal_vector=Vector([0.187, 0.352, -1.873]), constant_term=-1.991)
p3 = Plane(normal_vector=Vector([0.374, 0.704, -3.746]), constant_term=-3.982)
p4 = Plane(normal_vector=Vector([-0.561, -1.056, 5.619]), constant_term=5.973)
s = LinearSystem([p1, p2, p3, p4])
# r = s.compute_rref()
# print r
print s.do_gaussian_elimination_and_parametrize_solution()