import json
from src.config import students_file, marks_file

# ---------------- STUDENTS ---------------- #

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

    for s in students:
        if str(s["student_id"]) == str(student_id):
            print("Student already exists")
            return

    students.append({
        "student_id": str(student_id),
        "name": name,
        "age": age,
        "class_name": class_name
    })

    save_students(students)

def get_students():
    return load_students()

def delete_students(student_id):
    students = load_students()
    students = [s for s in students if str(s["student_id"]) != str(student_id)]
    save_students(students)

def update_student(student_id, name, age, class_name):
    students = load_students()

    for s in students:
        if str(s["student_id"]) == str(student_id):
            s["name"] = name
            s["age"] = age
            s["class_name"] = class_name

    save_students(students)

# ---------------- MARKS ---------------- #

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
    data = load_marks()

    data.append({
        "student_id": str(student_id),
        "subject": subject,
        "marks": int(marks)
    })

    save_marks(data)

def get_marks_by_student(student_id):
    data = load_marks()
    return [m for m in data if str(m["student_id"]) == str(student_id)]

# ---------------- CALCULATIONS ---------------- #

def calculate_percentage(student_id):
    marks = get_marks_by_student(student_id)

    if not marks:
        return 0

    total = sum(m["marks"] for m in marks)
    return total / len(marks)

def calculate_gpa(student_id):
    percentage = calculate_percentage(student_id)
    return round(percentage / 10, 2)

# ---------------- SEARCH / FILTER ---------------- #

def search_students(keyword):
    students = load_students()
    keyword = keyword.lower()

    return [
        s for s in students
        if keyword in s["name"].lower() or keyword in s["student_id"]
    ]

def filter_students_by_class(class_name):
    students = load_students()

    return [
        s for s in students
        if s["class_name"].lower() == class_name.lower()
    ]

# ---------------- PERFORMANCE METRICS ---------------- #

def get_all_percentages():
    students = load_students()
    result = []

    for s in students:
        percentage = calculate_percentage(s["student_id"])
        result.append({
            "student_id": s["student_id"],
            "name": s["name"],
            "percentage": percentage
        })

    return result

def get_topper():
    data = get_all_percentages()
    return max(data, key=lambda x: x["percentage"]) if data else None

def get_class_average():
    data = get_all_percentages()
    return sum(d["percentage"] for d in data) / len(data) if data else 0

def get_rank_list():
    data = get_all_percentages()
    return sorted(data, key=lambda x: x["percentage"], reverse=True)