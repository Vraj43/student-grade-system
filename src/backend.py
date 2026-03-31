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
    
    for student in students:
        if student["student_id"] == student_id:
            print("Student already exists")
            return 
        
    new_student={
        "student_id":student_id,
        "name":name,
        "age":age,
        "class_name":class_name
    }
    
    students.append(new_student)
    
    save_students(students)

def update_student(student_id,new_name,new_age,new_class):
    students=load_students()
    
    found = False
    for student in students:
        if student["student_id"] == student_id:
            student["name"] = new_name
            student["age"] = new_age
            student["class_name"] = new_class
            found = True
            
    if not found:
        print("Student Not Found")
        
    save_students(students)

def delete_students(student_id):
    students = load_students()
    
    updated_students = []
    
    for student in students:
        if student["student_id"] != student_id:
            updated_students.append(student)

    save_students(updated_students)

def get_students():
    return load_students()