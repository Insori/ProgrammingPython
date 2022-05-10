games = {"LOL","Overwatch","Tetris", 1942,2048}
print(games)    #집합(출력할 때마다 순서가 바뀜)
empty_set = {}  #빈 dixtionary
empty_set = set()   #빈 set
print(set({'google': 'google.com', 18: 'unesco.org'}))      #출력할 때마다 순서가 바뀜

#요소 추가
games.add("테일즈러너")
print(games)
games.update(("카트라이더","지렁이"))
print(games)

#요소 제거
games.remove("LOL")
print(games)

#set 연산
#교집합
#합집합
#차집합
#대칭 차집합
#p56, 57 실습 하자
#p57 표*****
a = set()
a.add('밥')
a.add('국')
print(a)
a.add('밥')
print(a)    #중복 제거
idol = ['세븐틴','스트레이키즈','악동뮤지션','방탄소년단','방탄소년단']
print(idol)
print(list(set(idol)))  #중복제거: set() -> list()