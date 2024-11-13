class StudentDetails:
    def __init__(self, firstname, lastname, age, DOB, address, course, fee, collegename, rollnumber):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.DOB = DOB
        self.address = address
        self.course = course
        self.fee = fee
        self.collegename = collegename
        self.rollnumber = rollnumber

    def display(self):
        print("STUDENT DETAILS")
        print("FULL NAME:", self.firstname, self.lastname)
        print("AGE:", self.age)
        print("DOB:", self.DOB)
        print("ADDRESS:", self.address)
        print("COURSE:", self.course)
        print("FEE:", self.fee)
        print("COLLEGE NAME:", self.collegename)
        print("ROLL NUMBER:", self.rollnumber)

# Collecting student details from user input        
def enter_StudentDetails():
    firstname = input("Enter the student first name: ")
    lastname = input("Enter the student last name: ")
    age = int(input("Enter age: "))
    dob = input("Enter DOB: ")
    address = input("Enter address: ")
    course = input("Enter Course: ")
    fee = float(input("Enter Fee: "))  # Ensure fee is float if needed
    collegename = input("Enter College Name: ")
    rollnumber = int(input("Enter Roll Number: "))

    # Creating a student object
    student = StudentDetails(firstname, lastname, age, dob, address, course, fee, collegename, rollnumber)
    return student  # Return the student object

# Create student object by calling the function
student = enter_StudentDetails()

# Displaying the stored student details

student.display()
