grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
def average_score(grades_list):
    return sum(grades_list) / len(grades_list)
result = {student: average_score(grades[list(students).index(student)]) for student in students}
print(result)