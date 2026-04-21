"""
-----------------------------------------------------------------------
ASSIGNMENT 14A: Object practice
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Define a class for a part of your project using PascalCase.
[ ] 3. Use __init__ to set private attributes (__variable).
[ ] 4. Write Setters and Getters for the attributes.
[ ] 5. Write a summary function that returns a formatted description.
[ ] 6. Instantiate two distinct objects and print their summaries.
-----------------------------------------------------------------------
"""

class Student:
    def __init__(self, first_name, last_name, student_id, gpa):
        # Double underscores make these private
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_id = student_id
        self.__gpa = gpa

    # --- GETTERS ---
    def get_first_name(self):
        return self.__first_name

    def get_gpa(self):
        return self.__gpa

    # --- SETTERS
    def set_gpa(self, new_gpa):
        # GPA must be between 0.0 and 4.0
        if 0.0 <= new_gpa <= 4.0:
            self.__gpa = new_gpa

    def set_first_name(self, new_name):
        self.__first_name = new_name

    # --- SUMMARY METHOD ---
    def get_student_report(self):
        """Returns a formatted string of the student's status."""
        return (f"STUDENT RECORDS\n"
                f"Name: {self.__first_name} {self.__last_name}\n"
                f"ID: {self.__student_id}\n"
                f"Current GPA: {self.__gpa}\n")

def main():
    print("--- Academic Management System ---\n")

    # 1. Instantiate two distinct objects (Two different students)
    student1 = Student("James", "Miller", "S1001", 3.5)
    student2 = Student("Sarah", "Chen", "S1002", 3.8)

    # 2. Use a Setter to update a GPA
    student1.set_gpa(3.7)

    # 3. Print their summaries using the summary method
    print(student1.get_student_report())
    print("-" * 25)
    print(student2.get_student_report())

    # 4. Use a Getter to pull a specific piece of data
    print(f"Notification: {student1.get_first_name()}'s records have been updated.")

if __name__ == "__main__":
    main()