# 1. 휴대전화번호 입력하면 -, /, 띄어쓰기 없애고 숫자만 출력하자
phone_number = '010-5062-6790'
# for i in phone_number:
#     if i=='-' or i=='/' or i==' ':
#         continue
#     else:
#         print(i, end='')
# print()
phone_number=phone_number.replace('-','')   #'-'를 ''로 바꿔준다.
phone_number=phone_number.replace('/','')   #'/'를 ''로 바꿔준다.
phone_number=phone_number.replace(' ','')   #' '를 ''로 바꿔준다.
print(phone_number)

print('-'*20)

# 2. 학번 -> 학년, 반, 학과, 번호 출력하기
student_number='2208'
# if student_number[1]=='1' or student_number[1]=='2':
#     h='뉴미디어소프트웨어과'
# elif student_number[1]=='3' or student_number[1]=='4':
#     h='뉴미디어웹솔루션과'
# elif student_number[1]=='5' or student_number[1]=='6':
#     h='뉴미디어디자인과'
majors = ['','뉴미디어소프트웨어과', '뉴미디어소프트웨어과', '뉴미디어웹솔루션과', '뉴미디어웹솔루션과', '뉴미디어디자인과', '뉴미디어디자인과']
index = int(student_number[1])
h = majors[index]
print(f'{student_number[0]}학년 {student_number[1]}반 {h} {int(student_number[2:])}번')

print('-'*20)

