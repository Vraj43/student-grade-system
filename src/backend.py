import json
from src.config import students_file

def load_students():
    f=open(students_file,"r")
    data=json.load(f)
    return data

def save_students(data):
    f=open(students_file,"w")
    json.dump(data,f,indent=4)
    
def add_students(student_id, name, age, class_name):
    students = load_students()
    
    new_student={
        "student_id":student_id,
        "name":name,
        "age":age,
        "class_name":class_name
    }
    
    students.append(new_student)
    
    save_students(students)
    
def get_students():
    return load_students()