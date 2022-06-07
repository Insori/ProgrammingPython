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

