class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class RateblePerson:
    def __lt__(self, other):
        if type(self) == type(other):
            return self.get_average_rate() < other.get_average_rate()
        else:
            raise TypeError('Сравнивать можно только объекты одного типа!')

    def __gt__(self, other):
        if type(self) == type(other):
            return self.get_average_rate() > other.get_average_rate()
        else:
            raise TypeError('Сравнивать можно только объекты одного типа!')

    def get_average_rate_for_course(self, course):
        if len(self.grades.get(course)) > 0:
            return sum([rate for rate in self.grades.get(course)]) / len(self.grades.get(course))
        else:
            return 0
    def get_average_rate(self):
        full_rate_list = []
        if len(self.grades.keys()) > 0:
            return sum([self.get_average_rate_for_course(course) for course in self.grades.keys()]) / len(self.grades.keys())
        else:
            return 0


class Student(Person, RateblePerson):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def __str__(self):
        return f'{super().__str__()}\nСредняя оценка за лекции: {self.get_average_rate()}\n'\
               f'Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'

    def rate_lesson(self, lecturer, course, grade):
        if not (0 <= grade <= 10):
            return 'Ошибка! Лекторы оцениваются по 10-бальной шкале!'

        if not isinstance(lecturer, Lecturer):
            return 'Студенты могут оценивать только лекторов!'

        if course not in lecturer.courses_attached:
            return 'Лектор не ведет занятия по данному курсу!'

        if course not in self.courses_in_progress:
            return 'Оценивать лектора можно только в период прохождения курса!'

        if course in lecturer.grades:
            lecturer.grades[course] += [grade]
        else:
            lecturer.grades[course] = [grade]
        return 'Оценка добавлена!'


class Mentor(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        return super().__str__()


class Lecturer(Mentor, RateblePerson):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'{super().__str__()}\nСредняя оценка за лекции: {self.get_average_rate()}'


class Reviewer(Mentor):
    def __str__(self):
        return super().__str__()

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
