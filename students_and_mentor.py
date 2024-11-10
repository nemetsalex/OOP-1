class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def rate_average(self):
        rate_sum = 0
        rate_count = 0
        for course in self.grades:
            rate_sum += sum(self.grades[course])
            rate_count += len(self.grades[course])
        return rate_sum / rate_count
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return "Сравниваются не студенты!"
        if self.rate_average() == other.rate_average():
            return f'Студенты равноценны!'
        if self.rate_average() > other.rate_average():
            return f'Студент {student_1.name} {student_1.surname} лучше учится, чем студент {student_2.name} {student_2.surname}!'
        else:
            return f'Студент {student_2.name} {student_2.surname} лучше учится, чем студент {student_1.name} {student_1.surname}!'
        
    def get_course(self):
        return ', '.join(map(str, self.courses_in_progress)) 
    
    def finish_course(self):
        return ', '.join(map(str, self.finished_courses))                   
        
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {round(self.rate_average(), 1)}\nКурсы в процессе изучения: {self.get_course()}\nЗавершенные курсы: {self.finish_course()}'
   
      
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
  
 
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return "Сравниваются не лекторы!"
        if self.rate_average() == other.rate_average():
            return f'Лекторы равноценны!'
        if self.rate_average() > other.rate_average():
            return f'Лектор {lectot_1.name} {lectot_1.surname} круче, чем лектор {lectot_2.name} {lectot_2.surname}!'
        else:
            return f'Лектор {lectot_2.name} {lectot_2.surname} круче, чем лектор {lectot_1.name} {lectot_1.surname}!'
        
    def rate_average(self):
        rate_sum = 0
        rate_count = 0
        for course in self.grades:
            rate_sum += sum(self.grades[course])
            rate_count += len(self.grades[course])
        return rate_sum / rate_count

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self.rate_average(), 1)}'


class Reviewer(Mentor):
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


def rate_average_students(list_students, course):    
    rate_sum = 0
    rate_count = 0
    for student in list_students:
        if isinstance(student, Student) and course in student.courses_in_progress:
            rate_sum += sum(student.grades[course])
            rate_count += len(student.grades[course])
        else:
            return 'Ошибка'
    return round(rate_sum / rate_count, 1)


def rate_average_lectors(list_lectors, course):    
    rate_sum = 0
    rate_count = 0
    for lector in list_lectors:
        if isinstance(lector, Lecturer) and course in lector.courses_attached:
            rate_sum += sum(lector.grades[course])
            rate_count += len(lector.grades[course])
        else:
            return 'Ошибка'
    return round(rate_sum / rate_count, 1)


student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Mat', 'Grag', 'your_gender')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']
student_2.finished_courses += ['Работа в Loop']
 
reviewer_1 = Reviewer('Van', 'Gog')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Wong', 'Bing')
reviewer_2.courses_attached += ['Git']
 
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_1, 'Git', 9)
reviewer_2.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Git', 10)
 
# print(student_1.grades)
# print(student_2.grades)

lectot_1 = Lecturer('Some', 'Buddy')
lectot_1.courses_attached += ['Python']
lectot_1.courses_attached += ['Git']

lectot_2 = Lecturer('Moon', 'Tuddy')
lectot_2.courses_attached += ['Python']
lectot_2.courses_attached += ['Git']

student_1.rate_lector(lectot_1, 'Python', 10)
student_1.rate_lector(lectot_1, 'Python', 9)
student_1.rate_lector(lectot_1, 'Python', 10)
student_1.rate_lector(lectot_2, 'Python', 9)
student_1.rate_lector(lectot_2, 'Python', 9)
student_1.rate_lector(lectot_2, 'Python', 9)
student_1.rate_lector(lectot_1, 'Git', 10)
student_1.rate_lector(lectot_1, 'Git', 10)
student_1.rate_lector(lectot_2, 'Git', 9)
student_1.rate_lector(lectot_2, 'Git', 10)

student_2.rate_lector(lectot_1, 'Python', 10)
student_2.rate_lector(lectot_1, 'Python', 10)
student_2.rate_lector(lectot_2, 'Python', 8)
student_2.rate_lector(lectot_2, 'Python', 10)
student_2.rate_lector(lectot_1, 'Git', 9)
student_2.rate_lector(lectot_1, 'Git', 10)
student_2.rate_lector(lectot_2, 'Git', 10)
student_2.rate_lector(lectot_2, 'Git', 9)

# print(lectot_1.grades)
# print(lectot_2.grades)

print()
print('--- ПРОВЕРЯЮЩИЕ ---------------')
print()
print(reviewer_1)
print()
print(reviewer_2)

print()
print('--- ЛЕКТОРЫ --------------------')
print()
print(lectot_1)
print()
print(lectot_2)
print()
print(lectot_1 == lectot_2)

print()
print('--- СТУДЕНТЫ -------------------')
print()
print(student_1)
print()
print(student_2)
print()
print(student_1 == student_2)
print()
print('--------------------------------')
print()

students = [student_1, student_2] 
print(f'Средняя оценка за ДЗ по всем студентам в рамках курса Python - {rate_average_students(students, "Python")}')
print(f'Средняя оценка за ДЗ по всем студентам в рамках курса Git    - {rate_average_students(students, "Git")}')
print()

lectors = [lectot_1, lectot_2] 
print(f'Средняя оценка за лекции всех лекторов в рамках курса Python - {rate_average_lectors(lectors, "Python")}')
print(f'Средняя оценка за лекции всех лекторов в рамках курса Git    - {rate_average_lectors(lectors, "Git")}')
print()