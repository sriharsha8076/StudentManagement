from student import Student


class StudentManager:
    """Manages a collection of students."""

    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, grade):
        """Add a new student to the system."""
        if student_id in self.students:
            print(f"Student with ID {student_id} already exists.")
            return None
        student = Student(student_id, name, age, grade)
        self.students[student_id] = student
        print(f"Student {name} added successfully.")
        return student

    def remove_student(self, student_id):
        """Remove a student from the system."""
        if student_id in self.students:
            removed = self.students.pop(student_id)
            print(f"Student {removed.name} removed.")
            return True
        print(f"Student with ID {student_id} not found.")
        return False

    def get_student(self, student_id):
        """Retrieve a student by their ID."""
        return self.students.get(student_id, None)

    def list_students(self):
        """List all students in the system."""
        if not self.students:
            print("No students enrolled.")
            return []
        for student in self.students.values():
            print(student)
        return list(self.students.values())

    def search_by_name(self, name):
        """Search students by name (case-insensitive)."""
        results = [
            s for s in self.students.values()
            if name.lower() in s.name.lower()
        ]
        return results

    def get_total_count(self):
        """Return the total number of students."""
        return len(self.students)
