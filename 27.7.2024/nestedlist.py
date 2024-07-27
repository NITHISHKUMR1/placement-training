if __name__ == '__main__':
    n = int(input().strip())
    students = []
    for _ in range(n):
        name = input().strip()
        grade = float(input().strip())
        students.append([name, grade])
    grades = sorted(set([grade for name, grade in students]))
    second_lowest_grade = grades[1]
    second_lowest_students = [name for name, grade in students if grade == second_lowest_grade]
    second_lowest_students.sort()
    for name in second_lowest_students:
        print(name)
