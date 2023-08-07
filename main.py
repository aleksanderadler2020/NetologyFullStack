from students_and_mentor import *


# Инициализируем менторов и студентов
student_1 = Student('Student', 'First')
student_1.courses_in_progress.append('Python')
student_1.courses_in_progress.append('Git')
student_1.finished_courses.append('Java')

student_2 = Student('Student', 'Second')
student_2.courses_in_progress.append('Python')
student_2.courses_in_progress.append('Git')
student_2.finished_courses.append('Java Script')

lecturer_1 = Lecturer('Lecturer', 'First')
lecturer_1.courses_attached.append('Python')
lecturer_1.courses_attached.append('Git')
lecturer_1.courses_attached.append('Java')

lecturer_2 = Lecturer('Lecturer', 'Second')
lecturer_2.courses_attached.append('Python')
lecturer_2.courses_attached.append('Git')

reviewer_1 = Reviewer('Reviewer', 'First')
reviewer_1.courses_attached.append('Python')
reviewer_1.courses_attached.append('Git')
reviewer_2 = Reviewer('Reviewer', 'Second')
reviewer_2.courses_attached.append('Python')
reviewer_2.courses_attached.append('Git')

# Оцениваем лекторов
student_1.rate_lesson(lecturer_1, 'Python', 5)
student_1.rate_lesson(lecturer_1, 'Git', 4)
student_2.rate_lesson(lecturer_1, 'Python', 6)
student_2.rate_lesson(lecturer_1, 'Git', 5)
student_1.rate_lesson(lecturer_2, 'Python', 7)
student_1.rate_lesson(lecturer_2, 'Git', 6)
student_2.rate_lesson(lecturer_2, 'Python', 8)
student_2.rate_lesson(lecturer_2, 'Git', 7)

# Оцениваем студентов
reviewer_1.rate_hw(student_1, 'Python', 1)
reviewer_1.rate_hw(student_1, 'Git', 2)
reviewer_1.rate_hw(student_2, 'Python', 3)
reviewer_1.rate_hw(student_2, 'Git', 4)
reviewer_2.rate_hw(student_1, 'Python', 5)
reviewer_2.rate_hw(student_1, 'Git', 6)
reviewer_2.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Git', 8)


# Средняя оценка студентов и лекторов на курсе
# В принципе достаточно 1 функции принимающей объекты RateblePerson
# Класс RateblePerson должен содержать словарь grades
def get_average_student_rate(students, course):
    course_rates = [student.get_average_rate_for_course(course) for student in students if course in student.grades]
    if len(course_rates) > 0:
        return print('Средняя оценка студентов на курсе', course, sum(course_rates)/len(course_rates))
    else:
        return print('Средняя оценка студентов на курсе', course, 0)


def get_average_lecturer_rate(lecturers, course):
    course_rates = [lecturer.get_average_rate_for_course(course) for lecturer in lecturers if course in lecturer.grades]
    if len(course_rates) > 0:
        return print('Средняя оценка лекторов на курсе', course, sum(course_rates) / len(course_rates))
    else:
        return print('Средняя оценка лекторов на курсе', course, 0)


print(student_1)
print('')
print(lecturer_1)
print('')
print(reviewer_1)

if student_1 > student_2:
    print('Студент 1 поумней будет')
else:
    print('Студент 2 поумней будет')

if lecturer_1 < lecturer_2:
    print('Лектор 2 поумней будет')
else:
    print('Лектор 1 поумней будет')

print()

get_average_lecturer_rate([lecturer_1, lecturer_2], 'Git')
get_average_lecturer_rate([lecturer_1, lecturer_2], 'Python')
get_average_student_rate([student_1, student_2], 'Git')
get_average_student_rate([student_1, student_2], 'Python')
print('')

# Проверим ошибочный ввод
print(student_1.rate_lesson(reviewer_1, 'Python', 5))
print(student_1.rate_lesson(lecturer_1, 'Java script', 5))
print(student_1.rate_lesson(lecturer_1, 'Python', 11))
print(student_1.rate_lesson(lecturer_1, 'Java', 5))

# сравнивать можно только объекты одного класса
# if student_1 > lecturer_1:
#     pass
