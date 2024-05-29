class Student:
    def __init__(self, first, last, gpa):
        self.first = first
        self.last = last
        self.gpa = gpa

    def get_gpa(self):
        return self.gpa

    def get_last(self):
        return self.last

class Course:
    def __init__(self):
        self.roster = []

    def add_student(self, student):
        self.roster.append(student)

    def course_size(self):
        return len(self.roster)

    # YOUR CODE
    # Returns the number of students with a GPA below 2.0
    def count_probation(self):
        count = 0
        for student in self.roster:
            if student.gpa < 2.0:
                count += 1
        return count

    # YOUR CODE
    # Returns the Student object with the highest GPA in the course. Assume that no 2 students have the
    # same highest GPA
    def find_student_highest_gpa(self):
        gpa_student = self.roster[0]
        for student in self.roster:
            if student.gpa > gpa_student.gpa:
                gpa_student = student

        return gpa_student


    # YOUR CODE
    # Outputs a list of all students enrolled in a course and also the total number of students in the course
    def print_roster(self):
        for student in self.roster:
            print(student.first, student.last, '( GPA:', student.gpa, ')')
        print(f'Students: {len(self.roster)}')


if __name__ == "__main__":
    course = Course()
    course.add_student(Student('Henry', 'Cabot', 3.5))
    course.add_student(Student('Brenda', 'Stern', 2.0))
    course.add_student(Student('Jane', 'Flynn', 3.9))
    course.add_student(Student('Lynda', 'Robison', 3.2))

    course.print_roster()

    student = course.find_student_highest_gpa()
    print('Top student:', student.first, student.last, '( GPA:', student.gpa,')')

    prob_count = course.count_probation()
    print('Probation count:', prob_count)