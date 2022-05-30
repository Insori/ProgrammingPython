# 문자열
for ch in "SORI":
    print(ch, end=' ')  # end=' ' - 뒤에 공백을 붙여라
print()

# 라스트
for item in ["힙합","발라드"]:
    print(item)

# 튜플
for item in (2929,39393):
    print(item)

for a,b in ((12,33), (2,35)):
    print(a,b)  #언패킹

# 셋
for item in {"WSM","JAVA","Python"}:
    print(item)

# 딕셔너리
pl = {"C":1972, "JAVA":1995, "Python":1991}
for item in pl:
    print(item) # key 값만 들어감

for key in pl.keys():
    print(key)  # "

for val in pl.values():
    print(val)  # calues 값만 나옴

for key,val in pl.items():  # iteams() : key, values 값 모두 보기
    print(key, val)

print()
# num_list 양수 찾기
num_list = [-5, 127, -13, 9, -21, 100]
for num in num_list:
    if num>0:
        print(num)

print()
# 짝수, 홀수
num_list = [13,8,7,55,100,2,12,10,17]
for num in num_list:
    if num%2==0:
        print(f'{num}은 짝수이다.')
    else:
        print(f'{num}은 홀수이다.')
print("----------------------")
holzzak = ["짝수","홀수"]
for num in num_list:
    print(f'{num}는 {holzzak[num%2]}이다.')

print()
# 자리수
for num in num_list:
    print(f'{num}은 {len(str(num))} 자리수이다.')

print()
# 실전 문제 - 합격 여부 판별
dream = {"마크":88,"재민":96,"천러":100,"런쥔":61,"지성":75,"제노":39,"해찬":55}
for name, score in dream.items():
    if score>=60:
        print(f'{name}은/는 합격입니다.')
    else:
        print(f'{name}은/는 불합격입니다.')

print()
# range() 함수
print(list(range(0,10,1)))
print(list(range(10,0,-1)))     # 증감값이 음수이면 역순
print(list(range(0,10,5)))

print(list(range(0,10)))    # 증감값의 기본값 = 0
print(list(range(10)))      # 시작값의 기본값 = 0


# 리스트
nctdream = ['런쥔','제노','해찬','마크','재민','지성','천러']
for member in nctdream:
    print(member)

for i in range(0,len(nctdream)):
    print(i+1, nctdream[i])
print("---------------------------------")
for i,member in enumerate(nctdream):
    print(i+1,member)
print()

# range() 문제
total = 0
for i in range(1,200):
    if i%3==0:
        total+=i
print(total)
print("------")
result = 0
for j in range(500,1000,5):
    if j%5==0:
        result+=j
print(result)

print()
#sum, max, min
l = [1,2,3,4,5]
print(sum(l))
print(max(l))
print(min(l))


# 구구단 - 2단 만들기
for i in range(1,10):
    print(f'2 X {i} = {2*i}')

print("------------------")
# 입력받아서 구구단 만들기
for i in range(2,10):
    for j in range(1,10):
        print(f'{i} X {j} = {i*j}')


