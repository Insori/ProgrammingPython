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

#10진수 -> 2진수
print(bin(10))      #0b1010
print(bin(9))       #0b1001
