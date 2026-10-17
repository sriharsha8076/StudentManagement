class Student:
    """Represents a student in the management system."""

    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.courses = []

    def enroll(self, course):
        """Enroll the student in a course."""
        if course not in self.courses:
            self.courses.append(course)
            return True
        return False

    def drop_course(self, course):
        """Drop a course for the student."""
        if course in self.courses:
            self.courses.remove(course)
            return True
        return False

    def get_info(self):
        """Return student information as a dictionary."""
        return {
            "id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
            "courses": self.courses,
        }

    def __str__(self):
        return f"Student({self.student_id}, {self.name}, Grade: {self.grade})"
