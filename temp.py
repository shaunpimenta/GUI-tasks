'''n = int(input("Enter number of elements in list: "))
A = list(map(int, input("Enter list elements: ").strip().split())) [:n]'''
#student_grades_updated = [value for value in student_grades if value[1] >= fail]

if __name__ == '__main__':
    stu_gra = []
    low_stu = []
    lowest = 100
    for _ in range(int(input(""))):
        name = input()
        score = float(input())
        stu_gra.append([name,score])
        if score < lowest:
            lowest = score
    print("student_grades: "+str(stu_gra))
    student_grades_updated = [value for value in student_gra if value[1] >= fail]
    print("updated student_grades: "+str(stu_gra_up))