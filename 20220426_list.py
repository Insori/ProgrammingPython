empty_list = [] #빈 리스트
player = ['Faker', 10, True]    #문자, 숫자, boolean - 다 들어갈 수 있음
print(len(empty_list))  #길이
print(len(player))
print(type(empty_list),type(player))    #<class 'list'> <class 'list'>
empty_list2 = list()    #list로 변환
print(len(empty_list2)) #0

message = list('miracle')
print(message)  #['m', 'i', 'r', 'a', 'c', 'l', 'e']
# numbers = list(56)    #타입 에러 - 숫자X
# print(numbers)
print(player)
player += [10,11]   #리스츠 풀려서 하나씩 추가
print(player)
player.append([20,21])  #리스트 통째로 추가
print(player)
player.append(56)   #⭐⭐⭐
print(player)
player.insert(2,'SKT T1')   #index, 값
print(player)
player.extend([30,31])  #+=랑 같음(풀려서 하나씩 추가)
print(player)
#append(): 리스트 통째로 추가
#insert(): index에 값 추가
#+=, extend(): 리스트 풀어서 하나씩 추가

player.append(40)   #끝에 40 추가
print(player)

#맨 끝에 50 추가 insert()
# player.insert(11,50)
#player.insert(-1,50)    #실패, 맨 마지막 두 번쨰에 추가, 40이 뒤로 밀림
player.insert(len(player),50)   #append()와 같음
print(player)
#수정
print(player[0:4])
print(player[0])
player[0] = '스티치'
print(player)
print(player[6][0])
player[6][0]=22
print(player)
print(player[6])
player[6] = 16
print(player)

#삭제
del player[2]   #인덱싱으로 지우기
print(player)
player.remove(30)   #값으로 지우기
print(player)
player.pop()    #맨 뒤에서 지우기
print(player)
player.pop(2)   #인덱스로 지우기
print(player)
# player.clear()  #리스트 초기화
# print(player)
#remove(): 값으로 지우기
#pop(index), del 리스트명[index]: 인덱스로 지우기
#pop(): 맨 뒤에서 지우기

print(100 in player)    #False
print(10 in player) #True
print('아이유' in player)  #False
# player.sort()   #에러 - 문자열과 숫자가 섞여 있어서 누가 큰 지 정렬 불가능
print(player)
player[0]=1
print(player)
player.sort()   #오름차순 정렬
print(player)
player.reverse()    #역순으로 뒤집기(내림차순 X)
print(player)

#***** range() - 범위
a = range(14)
print(a)    #range(0, 14)
a2 = list(a)    #리스트로 변환
print(a2)   #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(list(range(14)))  # 한 번에 쓰기
b = range(1, 14+1)  #(시작 숫자, 마지막 숫자 -1) - [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(list(b))
c = range(1,14+1,2)
print(list(c))
#range(stop): range(0, stop): 0, 1, 2, ..., stop-1
#range(start, stop): start, start+1, start+2, ..., stop-1
#range(start, stop, step): start, start+step, start+step+step, ..., stop-1
class1 = list(range(1, 14+1))
class2 = list(range(1, 14+1))
class3 = list(range(1, 14+1))
class3.remove(5)
class3.remove(10)
print(class3)

#Quiz. 두 자리 숫자 중 홀수인 숫자 리스트 출력하기
print(list(range(11, 99+1, 2)))

#Quiz. 한 자리 숫자 중 짝수인 숫자 거꾸로 리스트 출력하기
print(list(range(8, 0, -2)))
