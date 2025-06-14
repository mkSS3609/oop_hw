class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_finished_course(self, course_name):
        self.finished_courses.append(course_name)

    def add_course_in_progress(self, courses_name):
        """
        Метод добавления активных курсов
        (до этого использовался составной оператор присваивания (+=))
        """
        self.courses_in_progress.extend(courses_name)

    def rate_lecture(self, lecturer_, course, rate):
        """Средня оценка лектора"""
        if isinstance(lecturer_, Lecturer) and course in self.courses_in_progress and course in lecturer_.courses_attached:
            if course in lecturer_.grades:
                lecturer_.grades[course] += [rate]
            else:
                lecturer_.grades[course] = [rate]
        else:
            return 'Error'

    def average_score_hw(self):
        """Средня оценка студента"""
        rate_list = []
        if self.grades:
            for value in self.grades.values():
                rate_list.extend(value)
            return sum(rate_list) / len(rate_list)
        return None

    def __eq__(self, other):
        return self.average_score_hw() == other.average_score_hw()

    def __lt__(self, other):
        return self.average_score_hw() < other.average_score_hw()

    def __le__(self, other):
        return self.average_score_hw() <= other.average_score_hw()

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_score_hw()}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {', '.join(self.finished_courses)}')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_course_attached(self, courses_name):
        """
        Метод добавления активных курсов
        (до этого использовался составной оператор присваивания (+=))
        """
        self.courses_attached.extend(courses_name)

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_score_lecture(self):
        """Средня оценка лекторов"""
        rate_list = []
        if self.grades:
            for value in self.grades.values():
                rate_list.extend(value)
            return sum(rate_list) / len(rate_list)
        return None

    def __eq__(self, other):
        return self.average_score_lecture() == other.average_score_lecture()

    def __lt__(self, other):
        return self.average_score_lecture() < other.average_score_lecture()

    def __le__(self, other):
        return self.average_score_lecture() <= other.average_score_lecture()

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_score_lecture()}')

class Reviewer(Mentor):
    def rate_hw(self, student_, course, grade):
        if isinstance(student_, Student) and course in student_.courses_in_progress and course in self.courses_attached:
            if course in student_.grades:
                student_.grades[course] += [grade]
            else:
                student_.grades[course] = [grade]
        else:
            return 'Error'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')

#-----------------------------------------------------------------
students_list = []
lecturers_list = []

student1 = Student('Алёхина', 'Ольга', 'Ж')
students_list.append(student1)
student1.add_finished_course('Выбор профессии')
student1.add_finished_course('Введение в программирование')
student1.add_course_in_progress(['Python', 'Java'])

student2 = Student('Фокин', 'Дмитрий', 'М')
students_list.append(student2)
student2.add_finished_course('Введение в программирование')
student2.add_course_in_progress(['Python', 'C++'])

lecturer1 = Lecturer('Иван', 'Иванов')
lecturers_list.append(lecturer1)
lecturer1.add_course_attached(['Python', 'C++'])


lecturer2 = Lecturer('Андрей', 'Афонин')
lecturers_list.append(lecturer2)
lecturer2.add_course_attached(['Python', 'Java'])


reviewer1 = Reviewer('Пётр', 'Петров')
reviewer1.add_course_attached(['Python', 'C++'])
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 7)

reviewer2 = Reviewer('Александр', 'Тимарцев')
reviewer2.add_course_attached(['Python', 'Java'])
reviewer2.rate_hw(student1, 'Python', 8)
reviewer2.rate_hw(student2, 'Python', 8)

student1.rate_lecture(lecturer1, 'Python', 7)
student2.rate_lecture(lecturer1, 'Python', 8)
student1.rate_lecture(lecturer2, 'Python', 8)
student2.rate_lecture(lecturer2, 'Python', 6)

def average_score_all_students(student_list, course_name):
    grades_list = []
    for student in student_list:
        if isinstance(student, Student) and course_name in student.courses_in_progress and course_name in student.grades:
            grades_list.extend(student.grades[course_name])
    print(f'Средняя оценка за домашние задания по всем студентам в рамках конкретного курса ({course_name}):')
    if grades_list:
        print(f'{sum(grades_list) / len(grades_list)}\n')
    else:
        print(f'Оценки по данному предмету отсутствуют\n')

# average_score_all_students(students_list,'Java')

def average_score_all_lecturers(lecturer_list, course_name):
    grades_list = []
    for lecturer in lecturer_list:
        if isinstance(lecturer, Lecturer) and course_name in lecturer.courses_attached and course_name in lecturer.grades:
            grades_list.extend(lecturer.grades[course_name])
    print(f'Среднея оценка за лекции всех лекторов в рамках конкретного курса ({course_name}):')
    if grades_list:
        print(f'{sum(grades_list) / len(grades_list)}\n')
    else:
        print(f'Оценки за данные лекции отсутствуют\n')

# average_score_all_lecturers(lecturers_list, 'Java')

#-----------------------------------------------------------------
"""Проверка задания 1"""
def run_test_1():
    """
    Тестовые лектор и проверяющий созданы,
    дабы они имели пустые списки 'courses_attached'
    """
    test_lecturer = Lecturer('Тестовый', 'Лектор')
    test_reviewer = Reviewer('Тестовый', 'Проверяющий')
    print(isinstance(test_lecturer, Mentor))
    print(isinstance(test_reviewer, Mentor))
    print(test_lecturer.courses_attached)
    print(test_reviewer.courses_attached)
    print(f'------------\n')

"""Проверка задания 2"""
def run_test_2():
    print(student1.rate_lecture(lecturer1, 'Python', 9))
    print(student2.rate_lecture(lecturer1, 'Java', 8))
    print(student2.rate_lecture(lecturer2, 'С++', 8))
    print(student1.rate_lecture(reviewer1, 'Python', 10))
    print(lecturer1.grades)
    print(lecturer2.grades)
    print(f'------------\n')

"""Проверка задания 3"""
def run_test_3():
    print(reviewer1, '\n')
    print(reviewer2, '\n')
    print(lecturer1, '\n')
    print(lecturer2, '\n')
    print(student1, '\n')
    print(student2, '\n')
    print(student1 > student2, f'{student1.average_score_hw()} > {student2.average_score_hw()}')
    print(lecturer1 != lecturer2, f'{lecturer1.average_score_lecture()} != {lecturer2.average_score_lecture()}')
    print(f'------------\n')

"""Проверка задания 4"""
def run_test_4():
    average_score_all_students(students_list,'Python')
    average_score_all_students(students_list,'Java')

    average_score_all_lecturers(lecturers_list, 'Python')
    average_score_all_lecturers(lecturers_list, 'Java')

if __name__ == '__main__':
    run_test_1()
    run_test_2()
    run_test_3()
    run_test_4()