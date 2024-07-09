# 예외 처리 클래스들

# 잘못된 이름
class InvalidScore(Exception):
    pass


# 데이터 입력 갯수 이상할때
class InvalidDataCount(Exception):
    pass


# 중복 이름
class DuplicateName(Exception):
    pass


# 데이터 없음 즉 이름!!
class NoData(Exception):
    pass


# 이름 겹침
class NonExistentName(Exception):
    pass


# 그 2번에서 학점 부여안하면 오류뜸
class MissingGrade(Exception):
    pass


# 학생 정보를 저장할 리스트
students = []


##############  menu 1
def Menu1(student_name, midterm_score, final_exam_score):
    student_record = [student_name, midterm_score, final_exam_score]
    students.append(student_record)


##############  menu 2
def Menu2():
    for record in students:
        if len(record) != 4:
            average_score = (record[1] + record[2]) / 2
            if average_score >= 90:
                record.append('A')
            elif average_score >= 80:
                record.append('B')
            elif average_score >= 70:
                record.append('C')
            else:
                record.append('D')


##############  menu 3
def Menu3():
    print("--------------------------")
    print(f"{'name': <10}  {'mid':<3} {'final':<3} {'grade':<2}")
    print("--------------------------")
    for student in students:
        print(f"{student[0]:<10} {student[1]:<3} {student[2]:<3} {student[3]:<2}")



##############  menu 4
def Menu4(target_student_name):
    for record in students:
        if record[0] == target_student_name:
            students.remove(record)


# 학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")

while True:
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")

    if choice == "1":
        try:
            input_line = input("Enter name mid-score final-score : ")
            data_parts = input_line.split()
            student_name = data_parts[0]
            if len(data_parts) != 3:
                raise InvalidDataCount("Input data is length 3!")
            for record in students:
                if student_name == record[0]:
                    raise DuplicateName("Already existing name!")
            mid_exam_score, final_exam_score = map(int, data_parts[1:])
            if mid_exam_score <= 0 or final_exam_score <= 0:
                raise InvalidScore("Score is not a positive integer!")
            if mid_exam_score > 100 or final_exam_score > 100:
                raise InvalidScore("Score is not a positive integer!")
        except ValueError:
            print("Score is not a positive integer!")
        except DuplicateName as e:
            print(e)
        except InvalidScore as e:
            print(e)
        except InvalidDataCount as e:
            print(e)
        else:
            Menu1(student_name, mid_exam_score, final_exam_score)

    elif choice == "2":
        try:
            if len(students) == 0:
                raise NoData("No Student data!")
        except NoData as e:
            print(e)
        else:
            Menu2()
            print("Grading to all students.")

    elif choice == "3":
        try:
            if len(students) == 0:
                raise NoData("No Student data!")
            for record in students:
                if len(record) != 4:
                    raise MissingGrade("There is a student who didn't get a grade.")
        except NoData as e:
            print(e)
        except MissingGrade as e:
            print(e)
        else:
            Menu3()

    elif choice == "4":
        try:
            if len(students) == 0:
                raise NoData("No Student data!")
        except NoData as e:
            print(e)
        else:
            student_to_delete = input("Enter the name to delete : ")
            try:
                found = False
                for record in students:
                    if record[0] == student_to_delete:
                        found = True
                        break
                if not found:
                    raise NonExistentName("Not an existing name!")
            except NonExistentName as e:
                print(e)
            else:
                Menu4(student_to_delete)
                print(f"{student_to_delete} student information is deleted.")

    elif choice == "5":
        print("Exit Program!")
        break

    else:
        print("Wrong number. Choose again.")
