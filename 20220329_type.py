#숫자
student_number = 2212
age = 17
height = 169.9  #소수점도 됨


#문자
name = '인소리'
print(f'학번: {student_number}\n이름: {name}\n나이: {age}\n키: {height}')

print(type(student_number)) #<class 'int'>
print(type(name))   #<class 'str'>
print(type(age))    #<class 'int'>
print(type(height)) #<class 'float'>
print(type(10.27))  #<class 'float'>
print(type(1027))   #<class 'int'>
print(type('1027')) #<class 'str'>
print(10/27)    #java: 0, python: 0.37037037037037035
print(27/10)    #java: 2, python: 2.7
print(27//10)   #python: 나눈 몫: 2
print(27%10)    #python: 나머지: 7
print(type(10/27))  #<class 'float'>
print(type(10//27))   #<class 'int'>
print(type(10/5))    #<class 'float'>


#변수 이름 규칙, 자료형변환 - 변수,함수는 밑줄, 클래스는 대문자
#my_mbti, my_function(), MyClass        #java - myMbti: camel-case, JS - my_mbti: snake-case
my_mbti = 'INFP'
print(f'My MBTI: {my_mbti}')
#문자열+정수형 X
print('My MBTI:'+my_mbti+', age: '+str(age) )  #java: String.toString(age), python: str(age)
height = '170.0'
print(float(height)+10)     #java: Float.parseFloat(height), python: float(height)

#str(), float(), int(): 자료형변환 함수

# +연산자: 숫자+숫자: 숫자*숫자 => 덧셈, 문자+문자=>문자문자
# *연산자: 숫자*숫자 => 곱셈, 문자*숫자 => 문자를 숫자만큼 반복
print(18*2) #36
print('2'*4)    #'2222'

#짝을 10번 출력
print('짝'*10)

print(18 ** 3)  #거듭제곱

#진수 - java: 8진수 0o, 16진수 0x
print(0b10)     #2진수 10 => 2
print(0o10)     #8진수 10 => 8
print(0x10)     #16진수 10 => 16
print(0xFF)     #16진수 FF => 255

#10진수 -> 2진수, 8진수, 16진수
print(bin(10))      #0b1010
print(bin(9))       #0b1001
print(oct(10))      #0o12
print(hex(10))      #0xa

#지수 표현
print(f'지구의 나이: {4.543e9}살')    #float
print(f'원자의 크기: {1e-10}m')      #e를 단독으로 쓰면 변수로 인식해서 에러가 남 1e처럼 선언을 해줘야 함

#복소수
print(9+1j)     #j도 단독으로 쓸 수 없기 떄문에(변수로 인식) 1j로 선언  #결과에 ()가 있는 이유 : (9+1j)를 하나의 수로 봄
print(9+1j-4-5j)    #실수끼리, 허수끼리 계산 - (5-4j)
ys = 9+1j
hj = 7-3j
print(ys+hj)    #(16-2j)
print(ys.real)  #9.0
print(hj.imag)  #-3.0
print(hj.conjugate())   #켤레복소수
print(hj*hj.conjugate())    #(58+0j) = 49+(-3j * 3j) = 49+9 = (58+0j) - 복소수이기 때문에 j를 넣어줌
print(type(ys))     #<class 'complex'>
