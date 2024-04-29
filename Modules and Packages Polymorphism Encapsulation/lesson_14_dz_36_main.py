from lesson_14_dz_36_group import Group
from lesson_14_dz_36_student import Student
from lesson_14_dz_36_too_many_students_error import TooManyStudentsError

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert gr.find_student('Jobs') == st1
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr)

try:
    gr.add_student(Student('Male', 22, 'John', 'Doe', 'AN146'))
except TooManyStudentsError as e:
    print(e.message)

gr.delete_student('Taylor')
