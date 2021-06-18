class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}
        self.courses_attached = []

    def grading(self, lectur, course, grade):  # метод выставления оценок лекторам за лекции
        if isinstance(lectur, Lecturer) and course in lectur.courses_attached and course in self.courses_in_progress:
            # если лектор пристствует в классе Lecturer и курс в списке, закрепленных за этим лектором и студент этого класса изучает данный курс
            lectur.grades_lecturer += [grade]

        else:
            return 'Ошибка'

    def average_grades(self):
        for grade in self.grades.values():
            if len(grade) != 0:
                return round(sum(grade) / len(grade), 2)
            else:
                return 'Оценок нет'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нет такого студента')
            return
        return self.average_grades() < other.average_grades()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grades()}\n' \
               f'Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lecturer = []
        self.courses_attached = []  # нужен или нет здесь список?

    def average_grades_lecturer(self):
        if len(self.grades_lecturer) != 0:
            grade = sum(self.grades_lecturer) / len(self.grades_lecturer)
            return round(grade, 2)
        else:
            return 'Оценок нет'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нет такого лектора')
            return
        return self.average_grades_lecturer() < other.average_grades_lecturer()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grades_lecturer()}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student_1 = Student('Luka', 'Morozov', 'male')  # создаем обект - студента Луку
student_2 = Student('Lisa', 'Morozova', 'female')

reviewer_1 = Reviewer('Olga', 'Krasilnikova')  # создаем объект в классе проверяющих- Ольгу Красильникову
reviewer_2 = Reviewer('Lidia', 'Loginova')

lectur_1 = Lecturer('Darya', 'Belyakova')  # добавляем лектора- Дарью Белякову
lectur_2 = Lecturer('Kristina', 'Kornilova')

student_1.courses_in_progress += ['Python', 'Java']  # добавляем в список изучаемых курсов Пайтон
student_1.finished_courses += ['Python']  # добавляем список завершенных курсов
student_2.courses_in_progress += ['C#', 'Python']

reviewer_1.courses_attached += ['Python', 'Java']  # добавляем в список прикрепленных курсов к Красильниковой - Пайтон
reviewer_1.courses_attached += ['C#']
reviewer_2.courses_attached += ['C#', 'Python']

lectur_1.courses_attached += ['Python', 'C#']  # список преподаваемых курсов
lectur_2.courses_attached += ['Python', 'C#', 'Java']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Java', 8)
reviewer_1.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'C#', 10)
# print(student_1.grades)
# print(student_2.grades)

student_1.grading(lectur_1, 'Python', 9)
student_1.grading(lectur_1, 'C#', 7)
student_1.grading(lectur_2, 'Python', 10)
student_1.grading(lectur_2, 'Java', 10)
student_2.grading(lectur_1, 'C#', 8)
student_2.grading(lectur_1, 'Python', 9)
student_2.grading(lectur_2, 'Java', 10)
student_2.grading(lectur_2, 'Python', 10)

# print(lectur_1.grades_lecturer)
# print(lectur_2.grades_lecturer)
#
# print(reviewer_1)
# print()
# print(reviewer_2)
# print()
# print(lectur_1)
# print()
# print(lectur_2)
# print()
# print(student_1)
# print()
# print(student_2)
#
# print(lectur_1 < lectur_2)
# print(student_1 < student_2)

all_students = [student_1, student_2]


def average_grades_course(students, course):
    counter = 0
    av_grade = 0
    for student in students:
        for key, grade in student.grades.items():
            if key == course:
                av_grade += sum(grade) / len(grade)
                counter += 1
    return round(av_grade / counter, 2)


# print(average_grades_course(all_students, 'Python'))


all_lecturers = [lectur_1, lectur_2]


def average_grades_lecture(lecturers):
    counter = 0
    av_grade_lec = 0
    for lec in lecturers:
        av_grade_lec += sum(lec.grades_lecturer) / len(lec.grades_lecturer)
        counter += 1
    return round(av_grade_lec / counter, 2)


print(average_grades_lecture(all_lecturers))
