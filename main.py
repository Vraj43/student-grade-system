from src.backend import load_students,save_students,add_students,get_students
data=load_students()
print(data)

add_students(101,"Vraj",20,"sem4")
print(get_students())