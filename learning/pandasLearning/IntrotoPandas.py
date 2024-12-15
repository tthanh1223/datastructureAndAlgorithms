import pandas as pd


def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    # use a list of dictionaries
    students_list = []
    for student in student_data:
        student_dict = dict()
        student_dict['student_id'] = student[0]
        student_dict['age'] = student[1]
        students_list.append(student_dict)
    return pd.DataFrame(students_list)

def createDataframe_short_ver(student_data):
    return pd.DataFrame(data = student_data, columns = ['student_id', 'age'])

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    return list(players.shape)

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id'] == 101, ['name', 'age']]

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset = 'email',keep = 'first',inplace = True)
    return customers

if __name__ == "__main__":
    print(a)