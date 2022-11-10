if __name__ == '__main__':
#     for i in range(int(input("Total students"))):
#         name = input("Name")
#         score = float(input("Score"))
#         a= list(name)
#         b= list(score)
#
# print(a)

    n = int(input("Number of entries"))
    print("Enter name with marks ")
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = input("Enter query")
    marks = 0
    for i in student_marks[query_name]:
        marks = marks + i
        avg = marks / 3
    print("%.2f" % avg)