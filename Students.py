'''
File contains:
    - Main function for testing the program.
    - Class Course represnts a course, which contains a list of student objects as a courses roster
    - Class Student represents a classroom student, which has 3 attributes:
        - First name, Last name, GPA
'''
class Student:
    def __init__(self, first, last, gpa):
        self.first = first # first name
        self.last = last   # last name
        self.gpa = gpa     # grade point average

    def get_gpa(self):
        return self.gpa

    def get_last(self):
        return self.last

    def to_string(self):
        return self.first + ' ' + self.last + ' (GPA: ' + str(self.gpa) + ')'

class Course:
    def __init__(self):
        self.roster = []  # list of Student objects

    def add_student(self, student):
        self.roster.append(student)

    def count_students(self):
        return len(self.roster)


# Your Code Here
    # Students make the Dean's list if their GPS is 3.5 or higher. Complete the Course class by implementing
    # the get_deans_list() instance method, which returns a list of students with a GPA  of 3.5 or higher.
    # (hint: get_gpa() returns a student's GPA)
    def get_deans_list(self):
        deans_list = []
        for student in self.roster:
            if student.get_gpa() >= 3.5:
                deans_list.append(student)
        return deans_list

# Your Code Here
    # Complete the Course class by implementing the drop_student() instance method, which removes a student
    # (by last name) from the course roster. If the student isn't found in the course roster, no student
    # should be dropped
    # (hint: get_last() returns the last name field
    def drop_student(self, student):
        for students in self.roster:
            if students.last == student:
                self.roster.remove(students)



if __name__ == "__main__":
    course = Course()

    course.add_student(Student('Henry', 'Nguyen', 3.5))
    course.add_student(Student('Brenda', 'Stern', 2.0))
    course.add_student(Student('Lynda', 'Robinson', 3.2))
    course.add_student(Student('Sonya', 'King', 3.9))

    deans_list = course.get_deans_list()
    print("Dean's list:")
    for student in deans_list:
        print(student.to_string())

    print('Course size:', course.count_students(), 'students')
    course.drop_student('Stern')
    print('Course size after drop:', course.count_students(), 'students')