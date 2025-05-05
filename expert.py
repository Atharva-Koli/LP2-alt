#info
def manage_student():
    print("Managing Student Information:")
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    grade = input("Enter student's grade: ")
    print(f"Student {name}, age {age}, Grade {grade} has been added.\n")

def manage_faculty():
    print("Managing Faculty Information:")
    name = input("Enter faculty's name: ")
    dept = input("Enter faculty's department: ")
    salary = float(input("Enter faculty's salary: "))
    print(f"Faculty {name}, Department: {dept}, Salary: {salary} has been added.\n")

def manage_course():
    print("Managing Course Information:")
    course_name = input("Enter course name: ")
    course_code = input("Enter course code: ")
    credits = int(input("Enter number of credits: "))
    print(f"Course {course_name} ({course_code}) with {credits} credits has been added.\n")

def expert_system():
    print("Welcome to the Information Management System!")
    print("What would you like to manage today?")
    print("1. Student")
    print("2. Faculty")
    print("3. Course")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        manage_student()
    elif choice == 2:
        manage_faculty()
    elif choice == 3:
        manage_course()
    elif choice == 4:
        print("Exiting the system. Goodbye!")
        return
    else:
        print("Invalid choice. Please try again.")

    expert_system()  # Recursion for continuous operation

# Start the expert system
expert_system()

#medical
def manage_patient():
    print("Managing Patient Information:")
    name = input("Enter patient's name: ")
    age = int(input("Enter patient's age: "))
    disease = input("Enter diagnosed disease: ")
    doctor = input("Enter doctor's name: ")
    print(f"Patient {name}, age {age}, diagnosed with {disease}, under the care of Dr. {doctor} has been added.\n")

def manage_staff():
    print("Managing Staff Information:")
    name = input("Enter staff's name: ")
    role = input("Enter staff's role (Doctor, Nurse, etc.): ")
    department = input("Enter department (e.g., Surgery, Pediatrics): ")
    salary = float(input("Enter staff's salary: "))
    print(f"Staff {name}, role {role}, department {department}, Salary: {salary} has been added.\n")

def manage_medical_record():
    print("Managing Medical Record Information:")
    patient_name = input("Enter patient's name: ")
    record = input("Enter medical record description: ")
    doctor = input("Enter the attending doctor's name: ")
    print(f"Medical record for {patient_name} by Dr. {doctor}: {record} has been added.\n")

def hospital_management_system():
    print("Welcome to the Hospital and Medical Facilities Management System!")
    print("What would you like to manage today?")
    print("1. Patient")
    print("2. Staff")
    print("3. Medical Records")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        manage_patient()
    elif choice == 2:
        manage_staff()
    elif choice == 3:
        manage_medical_record()
    elif choice == 4:
        print("Exiting the system. Goodbye!")
        return
    else:
        print("Invalid choice. Please try again.")

    hospital_management_system()  # Recursion for continuous operation

# Start the hospital management system
hospital_management_system()


#employee
def evaluate_performance(attendance, teamwork, productivity):
    score = (attendance + teamwork + productivity) / 3
    
    if score >= 8:
        performance = "Excellent"
    elif score >= 6:
        performance = "Good"
    elif score >= 4:
        performance = "Satisfactory"
    else:
        performance = "Needs Improvement"
    
    return performance, score

def get_employee_data():
    name = input("Enter Employee Name: ")
    attendance = float(input("Enter Attendance Score (0-10): "))
    teamwork = float(input("Enter Teamwork Score (0-10): "))
    productivity = float(input("Enter Productivity Score (0-10): "))
    return name, attendance, teamwork, productivity

def employee_performance():
    name, attendance, teamwork, productivity = get_employee_data()
    performance, score = evaluate_performance(attendance, teamwork, productivity)
    print(f"\nEmployee: {name}")
    print(f"Performance Score: {score:.2f}")
    print(f"Performance: {performance}")

# Run the evaluation
employee_performance()
