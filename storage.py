import json
import os

file_name="students.json"

def load_students():
    if not os.path.exists(file_name):
        return []
    with open("students.json","r") as file:
        return json.load(file)

def save_students(students):
    with open(file_name, "w") as file:
        json.dump(students, file, indent=4)
def delete_students(students,uid):
    for student in students:
        if(student["uid"]==uid):
            students.remove(student)
            return True
    return False