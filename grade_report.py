class GradeReport:
    """Generates grade reports for students."""

    GRADE_POINTS = {
        "A": 4.0,
        "B": 3.0,
        "C": 2.0,
        "D": 1.0,
        "F": 0.0,
    }

    def __init__(self, student):
        self.student = student

    def get_gpa(self):
        """Calculate GPA based on student grade."""
        return self.GRADE_POINTS.get(self.student.grade.upper(), 0.0)

    def generate_report(self):
        """Generate a full grade report for the student."""
        gpa = self.get_gpa()
        report = (
            f"\n{'='*40}\n"
            f"  GRADE REPORT\n"
            f"{'='*40}\n"
            f"  Student ID : {self.student.student_id}\n"
            f"  Name       : {self.student.name}\n"
            f"  Age        : {self.student.age}\n"
            f"  Grade      : {self.student.grade}\n"
            f"  GPA        : {gpa:.2f}\n"
            f"  Courses    : {', '.join(self.student.courses) if self.student.courses else 'None'}\n"
            f"{'='*40}\n"
        )
        return report

    def is_honor_roll(self):
        """Check if student qualifies for honor roll (GPA >= 3.5)."""
        return self.get_gpa() >= 3.5
