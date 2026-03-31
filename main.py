from src.backend import add_students,get_students,update_student,delete_students

add_students(101,"Vraj Patel",20,"sem4")

update_student(101,"Vraj Patel",21,"sem5")

print(get_students())

delete_students(101)

print(get_students())