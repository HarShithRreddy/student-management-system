from storage import load_students, save_students, delete_students

def main():
    students = load_students()
    while True:
        code=int(input("Menu\n0.Exit\n1.Add Student \n2.Delete Student\n3.Display Students"))
        match code: 
            case 0:
                break;  
            case 1:
                while True:
                    name = input("Enter name: ")
                    uid = input("Enter uid: ")
                    sgpa = float(input("Enter sgpa: "))

                    students.append({
                        "name": name,
                        "uid": uid,
                        "sgpa": sgpa
                    })

                    if input("Add another? 1/0: ") != "1":
                        break

                save_students(students)      
            case 2:
                uid=input("Enter the uid of Student to be deleted ")
                if delete_students(students,uid):
                    print("Student deleted Successfully")
                    save_students(students)
                else: 
                    print("Student not found")
                
            case 3:
                print(load_students())


if __name__ == "__main__":
    main()