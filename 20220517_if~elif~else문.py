# 교통수단 문제
money = int(input('돈을 입력하시오 : '))
if money >= 10000:
    print("택시를 타라")
elif money >=720:
    print("버스를 타라")
else:
    print("그냥 걸어가라")

# 배수 판별 문제
num = int(input('정수를 입력하시오 : '))
if num%4==0:
    print("4의 배수")
elif num%3==0:
    print("3의 배수")
elif num%2==0:
    print("2의 배수")

# 나이대 판별 문제
age = int(input('나이를 입력하시오 : '))
if age>=10 and age<20:  #10<=age<20 가능
    print("10대")
elif age>=30 and age<40:    #30<=age<40 가능
    print("30대")
else:
    print("10대, 30대가 아님")

print("-------------------------")
print(str(age//10*10)+"대")  # 계산식으로 해결

# 논리연산자 문제
x = int(input('정수를 입력하시오 : '))
if x>10 and x%2==0:
    print("10 초과 짝수")

# 등급 판별 문제
score = int(input('점수를 입력하시오 : '))
if 100>=score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
elif score>=0:
    print("F")

# MBTI 판별 문제
MBTI = input('MBTI를 입력하시오 : ')
if MBTI == "INFP" or MBTI == "infp":    #MBTI.upper() == 'INFP'
    print("블록체인형")
elif MBTI == "ENFP" or MBTI == "enfp":
    print("AI형")
else:
    print("아직 개발중입니다")

# 10초과 짝수 홀수 판별 문제
x = int(input('정수를 입력하시오 : '))
if x>10:
    if x%2==0:
        print("10초과 짝수")
    else:
        print("10초과 홀수")
else:
    print("10이하")

# 아이디 패스워드 판별 문제
nickname = "sori"
user_ID= "insori"
user_PW = "zikzik"
ID = input('아이디를 입력하시오 : ')
if ID=="insori":
    PW = input('패스워드를 입력하시오 : ')
    if PW=="zikzik":
        print(f"환영합니다 {nickname}님")
    else:
        print("패스워드가 틀렸습니다.")
else:
    print("알 수 없는 사용자입니다.")



