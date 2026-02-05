# Problem: Nested Lists
# Platform: HackerRank

if __name__ == '__main__':
    students = []
    n = int(input())

    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name, score])

    lowest = min(student[1] for student in students)
    second_lowest = min(student[1] for student in students if student[1] != lowest)

    result = []
    for student in students:
        if student[1] == second_lowest:
            result.append(student[0])

    for name in sorted(result):
        print(name)
