# 예약어 X
# ㄴ snake_case
# 내장 함수와 이름이 같으면 에러는 안 나지만, 내장 함수는 호출할 수 없음
# ㄴ def sum(x):
#       print(x)
a = sum([10,20,3])
print(a)

print('-'*20)

'''
JAVA 함수
접근 제어자 리턴형 함수명(파라미터1, 파라미터 2) {
    return 값;
}

C 함수
리턴형 함수명(파라미터1, 파라미터2) {
    return 값;
}

PYTHON 함수
def 함수명(파라미터1, 파라미터2) :
    return 값
'''

def my_print(age):
    print(f'인소리: {age}살입니다.')   # 인소리: 17살입니다.
    # print('인소리: ',age,'살입니다.')  # 인소리:  17 살입니다.
print(my_print(17))    # my)print() 실행. my_print()의 리턴값 출력

print('-'*20)

def my_print2(name, age):
    print(f'{name}: {age}살입니다.')
    #print(name, ': ', age, '살입니다.')  # 사카타 긴토키 :  27 살입니다.
print(my_print2('사카타 긴토키',27))
print(my_print2(age=27, name='히지카타 토시로'))  # 아규먼트 순서와 관계없이 파라미터 이름을 쓰면 거기에 들어감

print('-'*20)

def my_print3(name, age, group):
    print(f'{name}: {age}살입니다. {group} 소속입니다.')
my_print3(name='오키타 소고',age=18, group='진선조')
#my_print3('오키타 소고', age=18, '은혼')   # <- 에러. 키워드 인자 뒤에는 계속 키워드 인자를 써줘야 함
my_print3('오키타 소고',age=18, group='진선조')
my_print3('오키타 소고', group='진선조',age=18)  # 위치 인자('오키타 소고')는 무조건 키워드 인자(group='진선조',age=18) 앞에 있어야 함

print('-'*20)

def my_print4(name, age, group='해결사'):   # 기본값 있는 파라미터
    print(f'{name}: {age}살입니다. {group} 소속입니다.')
my_print4('사카타 긴토키',age=18, group='은혼')  # group='은혼' 을 안 넣으면 기본값으로 '해결사'가 들어감

print('-'*20)

#가변 인자
def my_print5(*args):   # args 자료형은 tuple
    print('⁜정보⁜')
    for arg in args:
        print(arg)
my_print5('나재민', 23, 'NCT DREAM', 'BEATBOX')

def my_print6(name, *args):
    print(f'{name}의 ⁜정보⁜')
    for arg in args:
        print(arg)
my_print6('나재민', 23, 'NCT DREAM', 'BEATBOX')    # name에 '나재민'이 들어가고 *args에 23, 'NCT DREAM', 'BEATBOX'가 들어감

