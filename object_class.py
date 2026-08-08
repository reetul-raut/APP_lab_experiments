class Student:
    # Constructor
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    # Method to display student details
    def display(self):
        print("Student Details")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)

    # Method to check result
    def result(self):
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")


# Creating objects
student1 = Student("Alice", 101, 85)
student2 = Student("Bob", 102, 35)

# Calling methods
student1.display()
student1.result()
print("\n")
student2.display()
student2.result()
