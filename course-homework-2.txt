students_db = [
    "Ahmet Işık", "Mehmet Oluk", "Ayşe Gül", "Dilara Kazmıkçı"
]


def add_student(db, name_surname):
    return db.append(name_surname)


def remove_student(db, name_surname):
    return db.remove(name_surname)


def list_all_students(db):
    for i in db:
        print(i)


def student_no(db, name_surname):
    return db.index(name_surname) + 1


def add_multiple_students(db):
    while True:
        name_surname = input("İsim soyisim(çıkıs için enter):")
        if name_surname == "":
            break
        db.append(name_surname)


def remove_multiple_students(db):
    while True:
        name_surname = input("İsim soyisim(çıkıs için enter):")
        if name_surname == "":
            break
        db.remove(name_surname)


list_all_students(students_db)

print("*"*50)

add_student(students_db,"Arda Birişik")
print(students_db)

print("*"*50)

remove_student(students_db, "Arda Birişik")
print(students_db)

print("*"*50)

print(student_no(students_db,"Ahmet Işık"))

print("*"*50)

add_multiple_students(students_db)
print(students_db)

print("*"*50)

remove_multiple_students(students_db)
print(students_db)




