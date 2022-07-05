# 1~10까지 홀수의 제곱 리스트 만들기
array = []
for i in range(1,10,2):
    array.append(i*i)
print(array)

array = [i*i for i in range(1,10,2)]
print(array)

array = []
for i in range(1,10,2):
    if i*i > 30:
        array.append(i*i)
print(array)

array=[i*i for i in range(1,10,2) if i*i > 30]
print(array)