import json
def read_students(file_path: str) -> list:
    with open(file_path, 'r') as f:
        content = json.load(f)
    students = dict()
    for student in content:
        students[content[student]['name']] = content[student]['grades']
    return students

def find_max_avg_grades(students: dict) -> list:
    average_max = 0
    the_one = str()
    for student in students.items():
        average_point = sum(student[1])/len(student[1])
        if average_point > average_max:
            the_one = student[0]
            average_max = average_point
    return the_one, average_max



if __name__ == "__main__":
    file_path = "student.json"
    students  = read_students(file_path)
    student, average_max = find_max_avg_grades(students)
    print(f"{student}: {average_max:.02f}")