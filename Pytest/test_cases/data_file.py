import json
from datetime import date

Database = {
    '1': ['Marni', 'A', '24', '56'],
    '2': ['Veera', 'B', '25', '60'],
    '3': ['Venkata', 'A', '23', '57']
}


def save_dict(_dict, filepath):
    json.dump(_dict, open(filepath, 'w'))
    print('\n saved')


class Student:
    def __init__(self, name: str, dob: 'YYYY/ MM/ DD', branch: str, credit):
        self.name = name
        self.dob = dob
        self.branch = branch
        self.credits = 0
        self.courses = {credit[0]: credit[1]}

    def get_age(self):
        birth_date = self.dob.split('/')
        return date.today().year - int(birth_date[0]) - int((date.today().month, date.today().day) <
                                                            (int(birth_date[1]), int(birth_date[2])))

    # def add_credit(self, subject: str, value: float):
    #     self.courses[subject] = value
    #     self.credits += value

    def get_credits(self):
        # print(self.courses)
        return self.courses

    def delete_credits(self, course):
        self.courses.pop(course)

    def get_name(self):
        return self.name


def get_topper(students_list):
    score = 0.0
    stu_name = None
    for student in students_list:
        print(student)
        stu_score = list(student.get_credits().values())
        print(stu_score)
        if float(stu_score[0]) > score:
            score = stu_score[0]
            stu_name = student.get_name()
            print(stu_name)

    return stu_name, score


students = [Student('Veera', '1998/08/15', 'IT', ('Python', 4.0)),
            Student('Venkata', '199804/21', 'IT', ('Python', 4.5)),
            Student('Lakshmi', '1998/05/12', 'IT', ('Python', 4.3))]

get_topper(students)
