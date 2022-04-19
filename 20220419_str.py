greeting = 'hello'
to = 'world!'
say_hello = greeting+', '+ to
print(say_hello)
print(greeting*5)
print(greeting+'\n'+to)
print("\""+greeting+"\"")
print('\''+greeting+'\'')
#'''를 여러줄 주석으로 쓸 수 있음
#변수에 넣으면 출력 결과와 같음
names = '''양다연     
인소리
이예진
'''
print(names)

#*** indexing - 한 글자를 꺼내는 것 (시험에 나옴. 중요함)
names='양다연인소리이예진'
print(names[2]) #'연'
print(names[4]) #'소'
print(names[8]) #'진'

print(names[-1])    #'진'    -뒷 글자부터     -9 -8 -7 -6 -5 -4 -3 -2 -1
print(names[-2])    #'예'                    0  1  2  3  4  5  6  7  8
print(names[-9])    #'양'

student_number='2112'
print(student_number[0]+'학년')
print(f'{student_number[0]}학년')
print(f'{student_number[1]}반')

#*** slicing (시험에 나옴. 중요함)
print(names[2:5])   #[2]~[4] - [시작 글자~끝 글자+1]
print(names[2:4])   #연인
print(names[-7:-5])
print(names[4:7])   #소리이
print(names[7:9])   #예진
print(f'{student_number[2:4]}번')
print(f'{student_number[-2:]}번')    #[시작: ] - 끝까지
print(f'{student_number[0:2]}학년반')
print(f'{student_number[0:-2]}학년반')
print(f'{student_number[:-2]}학년반')  #[:끝] - 앞까지
print(f'{student_number[:]}')  #[:] - 앞에서 끝까지