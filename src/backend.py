import json
from src.config import students_file, marks_file

# ------------------ STUDENTS ------------------ #

def load_students():
    try:
        with open(students_file, "r") as f:
            return json.load(f)
    except:
        return []

def save_students(data):
    with open(students_file, "w") as f:
        json.dump(data, f, indent=4)

def add_students(student_id, name, age, class_name):
    students = load_students()

    for student in students:
        if str(student["student_id"]) == str(student_id):
            print("Student already exists")
            return

    new_student = {
        "student_id": str(student_id),
        "name": name,
        "age": age,
        "class_name": class_name
    }

    students.append(new_student)
    save_students(students)


def get_students():
    return load_students()


def delete_students(student_id):
    students = load_students()

    updated_students = [
        student for student in students
        if str(student["student_id"]) != str(student_id)
    ]

    save_students(updated_students)


def update_student(student_id, new_name, new_age, new_class):
    students = load_students()

    found = False

    for student in students:
        if str(student["student_id"]) == str(student_id):
            student["name"] = new_name
            student["age"] = new_age
            student["class_name"] = new_class
            found = True
            break

    if not found:
        print("Student not found")

    save_students(students)


# ------------------ MARKS ------------------ #

def load_marks():
    try:
        with open(marks_file, "r") as f:
            return json.load(f)
    except:
        return []

def save_marks(data):
    with open(marks_file, "w") as f:
        json.dump(data, f, indent=4)

def add_marks(student_id, subject, marks):
    all_marks = load_marks()

    new_record = {
        "student_id": str(student_id),
        "subject": subject,
        "marks": marks
    }

    all_marks.append(new_record)
    save_marks(all_marks)


def get_marks_by_student(student_id):
    all_marks = load_marks()

    return [
        record for record in all_marks
        if str(record["student_id"]) == str(student_id)
    ]


# ------------------ CALCULATIONS ------------------ #

def calculate_average(student_id):
    marks = get_marks_by_student(student_id)

    if not marks:
        return 0

    total = sum(int(m["marks"]) for m in marks)
    return total / len(marks)