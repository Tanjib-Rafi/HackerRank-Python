if __name__ == '__main__' :

    n = int(input())

    student_marks = {}

    for _ in range(n) :

        name, *line = input().split()

        scores = list(map(float, line))

        student_marks[name] = scores #key value pair

    query_name = input()

    marks = student_marks[query_name]

    solution = sum(marks) / len(marks)

    print( format(solution,'.2f') )