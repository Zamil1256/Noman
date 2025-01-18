students = [
    {'id': "01", 'name': "Md Noman Islam", 'dept': "Geology & Mining"},
    {'id': "02", 'name': "Ismail Akon", 'dept': "Chemistry"},
    {'id': "03", 'name': "Israfil Hawlader", 'dept': "Botany"},
    {'id': "04", 'name': "Akhi Kazi", 'dept': "Bangla"}
]
def loadDatabase():
    global students
    try:
        with open("mn.txt", "r") as file:
            for line in file:
                student = line.strip().split(",")
                students.append({"id": student[0], "name": student[1], "dept": student[2]})
                print(f"Added student: ID={student[0]}, Name={student[1]}, Department={student[2]}")
    except FileNotFoundError:
        print("Database not found. Starting with an empty database.")
        with open("mn.txt", "w") as file:
            pass
        print("New database File created.Starting with an empty database")
def updateDatabase():
    with open("mn.txt", "w") as file:
        for student in students:
            file.write(f"{student['id']},{student['name']},{student['dept']}\n")
def Main():
    print("Welcome to the Student Information System. Please choose an option from the menu below.")
    while (True):
        print("\nMain menu:\n──────────\n1. Add a New Student\n2. View All Students\n3. Search for a Student\n4. Edit a Student Profile\n5. Delete a Student Profile\n6. Exit")
        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            addStudent()
        elif choice == "2":
            viewStudent()
        elif choice == "3":
            searchStudent()
        elif choice == "4":
            editStudent()
        elif choice == "5":
            deleteStudent()
        elif choice == "6":
            print("\nThank you for using the system. Have a great day!")
            break
        else:
            print("\nInvalid choice. Please input a valid option.\n")

def addStudent(): 
    print("\nPlease enter a new Student ID. Ensure the ID is within 20 characters and does not contain spaces or special characters. Type 'X' to cancel.")
    while (True):
        id = input("Student Id : ").strip() 
        if (id == "X"):
            return
        elif (id == ""): 
            print("\nThe ID field can't be empty. Please try again.")
            continue 
        elif (len(id) >= 20): 
            print("\nThe ID field can't exceed 20 characters. Please try again.")
            continue 
        elif (id.isalnum() == False):
            print("\nThe ID must not contain space or special charecters. Please try again.")
            continue
        for student in students: 
            if (student['id'] == id):
                print("A Student with the same ID already exists.")
                return 
        break 
    print("\nPlease enter the student's name. The name must be between 3 to 50 characters. Type 'X' to cancel.")
    while (True):
        name = input("Student Name : ").strip()
        if (name == "X"):
            return
        elif (name == ""):
            print("The name field can't be empty. Please try again.")
            continue
        elif ((len(name)<3) or (len(name) > 50)):
            print("The name must be between 3 to 50 characters. Please try again.")
            continue
        elif (name.isdecimal() == True):
            print("The name can not be a numeric value. Please try again.")
            continue
        name = name.title()  
        break
    print("\nPlease enter the department name. The name must not exceed 50 characters. Type 'X' to cancel.")
    while (True):
        dept = input("Department Name : ").strip()
        if (dept == "X"):
            return
        elif (dept == ""):
            print("Field can't be empty. Please enter a valid department.")
            continue
        elif (len(dept) > 50):
            print("Department name can't exceed 30 characters. Please try again.")
            continue
        dept = dept.title()  
        break
    students.append({'id': id, 'name': name, 'dept': dept})
    updateDatabase()
    print("\nStudent information has been added successfully.\n")

def viewStudent():
    if (len(students) == 0):
        print("\nNo student information available.\n")
        return
    temp = sorted(students, key = lambda x:x["id"])
    a=[10]
    b=[12]
    c=[15]
    for i in students:
        a.append(len(i["id"]))
        b.append(len(i["name"]))
        c.append(len(i["dept"]))
    print("┌─" + "─" * max(a) + "─┬─" + "─" * max(b) + "─┬─" + "─" * max(c) + "─┐")
    print("│ " + "Student ID".center(max(a)) + " │ " + "Student Name".center(max(b)) + " │ " + "Department Name".center(max(c)) + " │")
    print("├─" + "─" * max(a) + "─┼─" + "─" * max(b) + "─┼─" + "─" * max(c) + "─┤")
    for student in temp:
        print("│ " + student["id"].center(max(a)) + " │ " + student["name"].ljust(max(b)) + " │ " + student["dept"].ljust(max(c)) + " │")
    print("└─" + "─" * max(a) + "─┴─" + "─" * max(b) + "─┴─" + "─" * max(c) + "─┘\n")

def searchStudent():
    search = input("\nEnter your queary to search: ").strip()
    temp = []
    n=1
    for student in students:
        if (search == student["id"]) or (search.lower() in student["name"].lower()) or (search.lower() in student["dept"].lower()):
            temp.append({'id': student["id"], 'name': student["name"], 'dept': student["dept"]})
    if len(temp) == 0:
        print(f"\nNo match found for {search}.\n")
    else:
        if len(temp)==1:
            print("\n1 match found for "+search+".\n"+"─"*(19+len(search)))
        else:
            print("\n"+str(len(temp))+" match's found for "+search+".\n"+"─"*(len(temp)+19+len(search)))
        for i in temp:
            if len(temp)>1:
                print(n,"\n──")
            print("Student ID      :", i["id"])
            print("Student Name    :", i["name"])
            print("Department Name :", i["dept"], "\n")
            n+=1
    return
    
def editStudent():
    id = input("\nEnter a valid student ID number: ").strip()
    for student in students:
        if student["id"] == id:
            print("\nWhat do you want to edit?\n1. ID number\n2. Name\n3. Department\n")
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                while (True):
                    new_id = input("Enter correct student ID : ").strip()
                    if (new_id == "X"):
                        return
                    elif (new_id == ""):
                        print("\nThe ID field can't be empty. Please try again.")
                        continue
                    elif (len(new_id) >= 20):
                        print("\nThe ID field can't exceed 20 characters. Please try again.")
                        continue
                    elif (new_id.isalnum() == False):
                        print("\nThe ID must not contain space or special charecters. Please try again.")
                        continue
                    break
                student["id"] = new_id
                print("\nStudent information updated successfully!\n")
            elif choice == "2":
                while (True):
                    new_name = input("Enter correct name : ").strip()
                    if (new_name == "X"):
                        return
                    elif (new_name == ""):
                        print("The name field can't be empty. Please try again.")
                        continue
                    elif ((len(new_name)<3) or (len(new_name) > 50)):
                        print("The name must be between 3 to 50 characters. Please try again.")
                        continue
                    elif (new_name.isdecimal() == True):
                        print("The name can not be a numeric value. Please try again.")
                        continue
                    new_name = new_name.title()
                    break
                student["name"] = new_name
                print("\nStudent information updated successfully!\n")
            elif choice == "3":
                while (True):
                    new_dept = input("Enter correct department name : ").strip()
                    if (new_dept == "X"):
                        return
                    elif (new_dept == ""):
                        print("Field can't be empty. Please enter a valid department.")
                        continue
                    elif (len(new_dept) > 50):
                        print("Department name can't exceed 50 characters. Please try again.")
                        continue
                    new_dept = new_dept.title()  # Capitalize the first letter of each word
                    break
                    student["dept"] = new_dept
                    print("\nStudent information updated successfully!\n")
                    
            else:
                print("\nInvalid choice. Please try again.\n")
            return
    print(f"\nNo student found with the ID: {id}.\n")
    return

def deleteStudent():
    print(r'To delete a student profile please enter the student ID. To delete multiple, type desired student IDs one after another followed by a comma(,). Type "ALL" to completely delete the whole database.')
    while(True):
        d = input("\nEnter a valid Student Id number: ").strip()
        delete = d.split(",")
        a=[]
        b=[]
        c=len(students)
        d=len(delete)
        if (len(d) == 0):
            print("You have to put something")
            continue
        if (d == "ALL"):
            for i in range(c):
                students.remove(students[0])
            print("Database cleared succesfully!")
            return
        for i in delete:
            for student in students:
                if (student["id"] == i.strip()):
                    students.remove(student)
                    a.append(i.strip())
                else:
                    b.append(i.strip())
        if (len(a)>0):
            print("\nStudent with ID number",",".join(a),"deleted successfully.\n")
        elif (len(b)>0):
            print("No student found with the ID number",",".join(b),".\n")
        break
        return
           
Main()
