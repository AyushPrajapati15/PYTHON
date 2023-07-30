# package in python

from university import info
info.getinfo()
print()

from university.students import bca
bca.bca_students()
bca.noofstudent
print()

from university.students import mca
mca.mca_students()
mca.noofstudent
print()

from university.teachers import teaching
teaching.teaching_teachers()
teaching.noofteachers
print()

from university.teachers import nonteaching
nonteaching.non_teaching_teachers()
nonteaching.noofteachers
print()

from university.students.bca import bca_students
bca_students()
from university.students.mca import mca_students
mca_students()
print()

from university.teachers.teaching import teaching_teachers
teaching_teachers()
print()

from university.teachers.nonteaching import non_teaching_teachers
non_teaching_teachers()
print()


from university import *
bca.bca_students()
bca.noofstudent
print()

mca.mca_students()
mca.noofstudent
print()

teaching.teaching_teachers()
teaching.noofteachers
print()

nonteaching.non_teaching_teachers()
nonteaching.noofteachers