# class Student:

#     def __init__(self, name, last_name, birth_year):
#         self.name = name
#         self.last_name = last_name
#         self.birth_year = birth_year
#         self.id = name[0] + last_name + birth_year


# new_student = Student(input(), input(), input())
# print(new_student.id)

def object_with_beautiful_identity():
    for i in range(10_000):
        if id(i) % 1000 == 888:
            return i
    return None

object_with_beautiful_identity()