from manager import StudentManager


def main():
    """Entry point for the Student Management System."""
    print("=== Student Management System ===")
    manager = StudentManager()

    # Add sample students
    manager.add_student(1, "Alice Johnson", 20, "A")
    manager.add_student(2, "Bob Smith", 21, "B")
    manager.add_student(3, "Carol White", 19, "A")

    print("\n--- All Students ---")
    manager.list_students()

    print(f"\nTotal students: {manager.get_total_count()}")

    # Enroll in courses
    alice = manager.get_student(1)
    alice.enroll("Mathematics")
    alice.enroll("Physics")
    print(f"\n{alice.name}'s courses: {alice.courses}")


if __name__ == "__main__":
    main()
