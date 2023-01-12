class Rope:
    def __init__(self, name, roll_no):
        self.name=name
        self.roll_no=roll_no
        self.college="Obafemi Awolowo University"

        print(f"The student name is: {self.name}")
        print(f"The student roll number is: {self.roll_no}")
        print(f"{self.name} attends {self.college}")


    def update_student_details(self, new_name, new_roll_no):
        self.name = new_name
        self.roll_no = new_roll_no


