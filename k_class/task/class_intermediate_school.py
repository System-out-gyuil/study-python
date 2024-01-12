# 학교
# 이름, 지역, 학생 수, 선생님 수
# 학교 정보 출력 메소드
class School:

    def __init__(self, school_name, school_address, student_count, teacher_count):
        self.school_name = school_name
        self.school_address = school_address

    def show_school(self, teacher, student):
        print(self.school_name, self.school_address, self.teacher.total_teacher, self.student.total_student)



# 선생님
# 이름, 과목, 학교
# 선생님이 추가될 때마다 선생님 수 1증가
# 준비된 학생들에게 해당 과목을 가르치면 학생들의 능력치 1증가
# 선생님 정보 출력 메소드
class Teacher:

    def __init__(self, teacher_name, subject, school, student):
        self.teacher_name = teacher_name
        self.subject = subject
        self.school = school
        self.student = student
        self.school.teacher_count += 1

    def show_teacher(self):
        print(self.teacher_name, self.subject, self.school)

    def teach(self, students):
        for student in students:
            student.ability += 1

# 학생
# 이름, 학년(grade), 학교, 능력치(초기값: 0), 담임 선생님
# 학생이 추가될 때마다, 학생 수 1증가
# 학생 정보 출력 메소드
class Student:

    def __init__(self, student_name, student_grade, teacher, school, abillity=0):
        self.student_name = student_name
        self.student_grade = student_grade
        self.abillity = abillity
        self.teacher = teacher
        self.school = school
        self.school.student_count += 1

    def show_student(self):
        print(self.student_name, self.student_grade, self.abillity, self.teacher, self.school)

school = School('아무중학교', '역삼동')
teacher = Teacher('홍길동', '도둑과목')
students = [
            Student('김규일', '3학년'),
            Student('가나다', '2학년'),
            Student('라마바', '1학년'),
            ]

print(school.show_school(teacher, student))

