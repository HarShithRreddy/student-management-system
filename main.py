from student import Student

def main():
    student_list = []
    i = 1
    while i:
        name = input("Enter the name of the student: ")
        uid = input("Enter the uid of the student: ")
        sgpa = float(input("Enter the sgpa of the student: "))
        s = Student(name, uid, sgpa)
        student_list.append(s)
        i = int(input("Want to add one more student? 1/0: "))

if __name__ == "__main__":
    main()