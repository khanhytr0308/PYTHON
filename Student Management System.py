student = {
    '001': {
        'name': 'An',
        'age': 19,
        'gpa': 3.5
    },
    '002': {
        'name': 'Bình',
        'age': 20,
        'gpa': 3.7
    }
}

def add_student():
    mssv = input("mssv: ")
    if mssv in student:
        print("already exists")
        return 1
    else:
        student[mssv] = {
            "name": input("name: "),
            "age": int(input("age: ")),
            "gpa": int(input("gpa: "))
        }

# if add_student():
#     print(student)

def find_student():
    mssv = input("dien mssv: ")
    if mssv in student:
        print("da tim thay")
        print(f"thong tin sv: {student[mssv]}")
    else:
        print("khong thay")
        
# find_student()

def remove_student():
    mssv = input("dien mssv: ")
    if mssv in student:
        del student[mssv]
        print("xoa thanh cong")
        return 1
    else:
        print("khong tim thay")

# if remove_student():
#     print(student)



