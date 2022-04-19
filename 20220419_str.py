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

#문자열 함수
print(f'길이: {len(student_number)}')    #4
print(f'2의 개수: {student_number.count("2")}')    #2
print(f'{"NCT dream darling".upper()}') #NCT DREAM DARLING
print(f'{"NCT dream darling".lower()}') #nct dream darling
s = "   NCT dream buffering   "
print(f'{s.strip()}')   #띄어쓰기가 벗겨짐
print(f'{s.lstrip()}')   #왼쪽 띄어쓰기가 벗겨짐
print(f'{s.rstrip()}')   #오른쪽 띄어쓰기가 벗겨짐
print(f'{s.find("d")}') #7
print(f'{s.find("z")}') #없으면 -1
print(f'{s.rfind("e")}')    #17
print(f'{s.count("e")}')    #2
print(f'{s.index("d")}') #7
#print(f'{s.index("z")}')    #없으면 ValueError: substring not found
print(f'{s.replace("buffering","hello future")}')   #이때만 바뀐 문자열로 리턴해줌(원본은 바뀌지 않음)
print(s)

print("e" in s)
print("z" in s)

#split, join
ip='10.253.123.119'
ip_list = ip.split('.')
print(ip_list)
names = '양다연, 최자윤, 임채영, 이예진, 인소리'
names_list=names.split(', ')
print(names_list)
print(names_list[2])    #임채영
print(names_list[2:4])    #임채영 이예진

ip_list_str='::'.join(ip_list)
print(ip_list_str)
names_list_str=' | '.join(names_list)
print(names_list_str)
print(','.join(names_list))


#format
s='name: {}, number: {}, soccer: {}'
print(s.format('손흥민',7,True))
s='name: {1}, number: {2}, soccer: {0}'
print(s.format('손흥민',7,True))
s='name: {name}, number: {n}, soccer: {s}'
print(s.format(name='손흥민',n=7,s=True))


