if __name__ == '__main__':
    n = int(input().strip())
    student_marks = {}
    for _ in range(n):
        line = input().strip().split()
        name = line[0]
        marks = list(map(float, line[1:]))
        student_marks[name] = marks
    query_name = input().strip()
    marks = student_marks[query_name]
    average_marks = sum(marks) / len(marks)
    print(f"{average_marks:.2f}")
