from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, email):
        self._name = name
        self._age = age 
        self._email = email
        
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    def get_age(self):
        return self._age
    def set_age(self, age):
        self._age = age
    def get_email(self):
        return self._email
    def set_email(self, email): 
        self._email = email

    @abstractmethod
    def get_role(self):
        pass
class Student(Person):
    def __init__(self, name, age, email):
        super().__init__(name, age, email)
        self._grades = []
    def add_grade(self, grade):
        self._grades.append(grade)
    def calculate_average(self):
        if not self._grades:
            return 0
        return sum(self._grades) / len(self._grades)
    def get_status(self):
        average = self.calculate_average()
        return "Pass" if average >= 70 else "Fail"
    def get_role(self):
        return "Student"
class Instructor(Person):
    def __init__(self, name, age, email, subject):
        super().__init__(name, age, email)
        self._subject = subject
    def assign_grade(self, student, grade):
        student.add_grade(grade)
    def get_role(self):
        return "Instructor"
class Course:
    def __init__(self, course_name):
        self._course_name = course_name
        self._students = []
        self._instructor = None
    def add_student(self, student):
        self._students.append(student)
    def set_instructor(self, instructor):
        self._instructor = instructor
    def generate_report(self):
        report = f"Course: {self._course_name}\n"
        report += f"Instructor: {self._instructor.get_name() if self._instructor else 'None'}\n"
        report += "Students:\n"
        for student in self._students:
            report += f"- {student.get_name()}, Average: {student.calculate_average():.2f}, Status: {student.get_status()}\n"
        return report
    def print_person_role(person):
        print(f"{person.get_name()} is a {person.get_role()}")
# Example usage
if __name__ == "__main__":
    # Create instructor
    instructor = Instructor("Dr. Smith", 45, "smith@example.com", "Mathematics")
    # Create students
    student1 = Student("Alice", 20, "alice@example.com")
    student2 = Student("Bob", 22, "bob@example.com")
    # Create course and assign instructor
    course = Course("Calculus 101")
    course.set_instructor(instructor)
    # Add students to course
    course.add_student(student1)
    course.add_student(student2)
    # Instructor assigns grades
    instructor.assign_grade(student1, 85)   
    instructor.assign_grade(student1, 90)
    instructor.assign_grade(student2, 65)
    instructor.assign_grade(student2, 70)
    # Generate and print course report
    print(course.generate_report())
    # Print roles
    Course.print_person_role(instructor)
    Course.print_person_role(student1)
    Course.print_person_role(student2)