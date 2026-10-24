#1
class Person:
    def __init__(self, name):
        self.name = name
    def info(self):
        return f"Ім'я: {self.name}"

class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group
    def info(self):
        return f'Учень: {self.name}, група: {self.group}'

student1 = Student("Anna Ivanenko", "IT-10")
student2 = Student("Ivan Potapenko", "МА-10")
# print(student1.info())
#2
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    def info(self):
        return f'Викладач: {self.name}, предмет: {self.subject}'

MixedList = [
    Person("David Schmorez"),
    student1,
    student2,
    Teacher("Svitlana Volodymirivna", "Maths")
]
# for person in MixedList:
#     print(person.info())

#3
class Course:
    def __init__(self, title, teacher, students = []):
        self.title = title
        self.teacher = teacher
        self.students = students

    def add_student(self, student):
        for stu in self.students:
            if stu.name.lower() == student.name.lower():
                return False
        self.students.append(student)
        return True

    def remove_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                self.students.remove(student)
                return True
        return False

    def show_students(self):
        print("Курс:",self.title)
        print("Викладач:",self.teacher.name)
        print("Студенти:")
        if len(self.students) > 0:
            for i,student in enumerate(self.students):
                print(f'{i+1}. {student.name}')
        else:
            print("Немає")

Math = Course("Maths",Teacher("Mykhailo Tadlya","Maths"))

Math.add_student(Student("Vadym Khrypliak","МА-9"))
Math.add_student(Student("Daria Gafarova","МА-10"))
Math.add_student(Student("Kriukow Vladislav","МА-9"))
Math.add_student(Student("Dmytro Oleksandrovych","МА-8"))

Math.add_student(Student("Vadym Khrypliak","ІТ-9"))

Math.remove_student("Dmytro Oleksandrovych")

Math.show_students()

#4
class Student(Person):
    def __init__(self, name, group, grades = []):
        super().__init__(name)
        self.group = group
        self.grades = grades

    def info(self):
        return f'Учень: {self.name}, група: {self.group}'

    def add_grade(self,grade):
        if grade >= 1 and grade <= 12:
            self.grades.append(grade)

    def average(self):
        if len(self.grades) > 0:
            return sum(self.grades) / len(self.grades)
        else:
            return 0

class Course():
    def __init__(self, title, teacher, students = []):
        self.title = title
        self.teacher = teacher
        self.students = students

    def add_student(self, student):
        for stu in self.students:
            if stu.name.lower() == student.name.lower():
                return False
        self.students.append(student)
        return True

    def remove_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                self.students.remove(student)
                return True
        return False
    def show_students(self):
        print("Курс:",self.title)
        print("Викладач:",self.teacher.name)
        print("Студенти:")
        if len(self.students) > 0:
            for i,student in enumerate(self.students):
                print(f'{i+1}. {student.name}')
        else:
            print("Немає")

    def find_student(self,name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def add_grade_to_student(self,name,grade):
        if self.find_student(name):
            if self.find_student(name).add_grade(grade):
                return True
            return False

    def show_rating(self):
        SortedStudents = self.students
        if len(self.students) > 0:
            SortedStudents = []
            curStu = 0
            for i in range(len(self.students)):
                fstu = Student("","",[0])
                for stud in self.students:
                    if not stud in SortedStudents:
                        if curStu < stud.average():
                            curStu = stud.average()
                            fstu = stud
                SortedStudents.append(fstu)
                curStu = 0
        print("Рейтинг:")
        for i,student in enumerate(SortedStudents):
            print(f'{i+1}. {student.name} — {student.average()}')

course = 0
try:
    with open("course_data.txt", "r", encoding="utf-8") as file:
        cd = file.readlines()
        for i,line in enumerate(cd): cd[i] = line.strip("\n")
        if len(cd) < 2:
            raise FileNotFoundError
        course = Course(cd[0],Teacher(cd[1],cd[0]))
        for line in cd[2:]:
            name,grades = line.split(";")
            grades = grades.split(",")
            if grades[0] != " ":
                for i,grade in enumerate(grades): grades[i] = int(grade)
                course.add_student(Student(name,cd[0],grades))
            else:
                course.add_student(Student(name,cd[0]))
except FileNotFoundError:
    with open("course_data.txt", "w", encoding="utf-8") as file:
        title = input("Назва курсу: ")
        print(f"{title}", file=file)
        Tname = input("Ім'я викладача: ")
        print(f"{Tname}", file=file)
        course = Course(title,Teacher(Tname,title))

print("1 — показати курс")
print("2 — додати студента")
print("3 — видалити студента")
print("4 — знайти студента")
print("5 — виставити оцінку")
print("6 — показати рейтинг")
print("0 — вихід.")

while True:
    command = input("\nДія: ")
    if command == "1":
        course.show_students()
    elif command == "2":
        name = input("Ім'я студента: ")
        if course.add_student(Student(name, course.title)):
            with open("course_data.txt", "a", encoding="utf-8") as file:
                print(f"{name};", file=file)
    elif command == "3":
        name = input("Ім'я студента: ")
        if course.remove_student(name):
            ignoredLine = 0
            cd = 0
            with open("course_data.txt", "r", encoding="utf-8") as file:
                cd = file.readlines()
                for i, line in enumerate(cd): cd[i] = line.strip("\n")
                for i, line in enumerate(cd):
                    if line.split(";")[0] == name:
                        ignoredLine = i
            with open("course_data.txt", "w", encoding="utf-8") as file:
                for i, line in enumerate(cd):
                    if i != ignoredLine:
                        print(line, file=file)
    elif command == "4":
        name = input("Ім'я студента: ")
        print(course.find_student(name).info())
    elif command == "5":
        name = input("Ім'я студента: ")
        grade = input("Оцінка: ")
        try:
            grade = int(grade)
            if course.add_grade_to_student(name,grade):
                cd = 0
                FixedLineNum = 0
                with open("course_data.txt", "r", encoding="utf-8") as file:
                    cd = file.readlines()
                    for i, line in enumerate(cd): cd[i] = line.strip("\n")
                    for i, line in enumerate(cd):
                        if line.split(";")[0] == name:
                            FixedLineNum = i
                with open("course_data.txt", "w", encoding="utf-8") as file:
                    for i, line in enumerate(cd):
                        if i != FixedLineNum:
                            print(line, file=file)
                        else:
                            if line[-1] != ";":
                                print(f'{line},{grade}', file=file)
                            else:
                                print(f'{line}{grade}', file=file)
            else:
                if grade < 1 or grade > 12:
                    print("Помилка: число має бути від 1 до 12")
                else:
                    print("Помилка: немає такого студента")
        except ValueError:
            print("Помилка: введіть оцінку як число")
    elif command == "6":
        course.show_rating()
    elif command == "0":
        break