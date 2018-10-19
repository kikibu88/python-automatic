student_info = {'홍길동' : 1234, '기범' : 8888}

student_name = input ("학생 이름을 입력하세요: ")

for d_name in student_info.keys():
    if student_name == d_name:
        student_number = student_info[d_name]
        print("이름 : %s"  %(student_name))
        print("학번 : %d"  %(student_number))
        break

