# University GPA & Scholarship System
class Subject:
    def __init__(self, name, marks, credit_hours):
        self.name = name
        self.marks = marks
        self.credit_hours = credit_hours

    def get_grade_point(self):
        if self.marks >= 85:
            return 4.0
        elif self.marks >= 80:
            return 3.67
        elif self.marks >= 75:
            return 3.33
        elif self.marks >= 70:
            return 3.0
        elif self.marks >= 65:
            return 2.67
        elif self.marks >= 60:
            return 2.0
        elif self.marks >= 50:
            return 1.0
        else:
            return 0.0
        
#Student class to hold student information and calculate GPA and scholarship status
class Student:
    def __init__(self, name, roll_no, department):
        self.name = name
        self.roll_no = roll_no
        self.department = department
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def calculate_gpa(self):
        total_quality_points = 0
        total_credit_hours = 0

        for subject in self.subjects:
            grade_point = subject.get_grade_point()
            total_quality_points += grade_point * subject.credit_hours
            total_credit_hours += subject.credit_hours

        if total_credit_hours == 0:
            return 0

        return round(total_quality_points / total_credit_hours, 2)

    def scholarship_status(self):
        gpa = self.calculate_gpa()

        if gpa >= 3.7:
            return "Merit Scholarship (Full)"
        elif gpa >= 3.3:
            return "Partial Scholarship"
        else:
            return "Not Eligible"

    def display_report(self):
        print("\n" + "=" * 55)
        print("STUDENT REPORT CARD")
        print("=" * 55)

        print(f"Name       : {self.name}")
        print(f"Roll No    : {self.roll_no}")
        print(f"Department : {self.department}")

        print("\nSubjects:")
        print("-" * 55)

        for subject in self.subjects:
            print(
                f"{subject.name:<20}"
                f"Marks: {subject.marks:<6}"
                f"CH: {subject.credit_hours:<4}"
                f"GP: {subject.get_grade_point()}"
            )

        print("-" * 55)
        print(f"GPA         : {self.calculate_gpa()}")
        print(f"Scholarship : {self.scholarship_status()}")
        print("=" * 55)


students = []

while True:
    print("\n===== UNIVERSITY GPA & SCHOLARSHIP SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Roll No")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":

        name = input("Enter Name: ")

        roll_no = input("Enter Roll No: ").strip().upper()

        if any(student.roll_no == roll_no for student in students):
            print("Student with this Roll No already exists!")
            continue

        department = input("Enter Department: ")

        student = Student(name, roll_no, department)

        try:
            num_subjects = int(input("Number of subjects: "))

            for i in range(num_subjects):

                print(f"\nSubject {i + 1}")

                subject_name = input("Subject Name: ")

                while True:
                    marks = float(input("Marks (0-100): "))
                    if 0 <= marks <= 100:
                        break
                    print("Marks must be between 0 and 100!")

                while True:
                    credit_hours = int(input("Credit Hours: "))
                    if credit_hours > 0:
                        break
                    print("Credit Hours must be greater than 0!")

                subject = Subject(
                    subject_name,
                    marks,
                    credit_hours
                )

                student.add_subject(subject)

            students.append(student)

            print("\nStudent Added Successfully!")

        except ValueError:
            print("\nInvalid input! Please enter valid numbers.")

    elif choice == "2":

        if not students:
            print("\nNo student records found.")

        else:
            for student in students:
                student.display_report()

    elif choice == "3":

        if not students:
            print("\nNo student records found.")

        else:
            search_roll = input("Enter Roll No to search: ").strip().upper()
            found = False

            for student in students:
                if student.roll_no == search_roll:
                    student.display_report()
                    found = True
                    break
            if not found:
                print("\nStudent not found!")

    elif choice == "4":
        print("\nProgram Closed Successfully.")
        break
    else:
        print("\nInvalid Choice! Please select 1-4.")