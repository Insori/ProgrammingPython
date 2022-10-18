# 클래스 변수: 객체로 생성하지 않아도 클래스에 하나 존재하는 변수
# 클래스 메소드: 객체로 생성하지 않아도 클래스에 하나 존재하는 메소드

# 학생
# 속성: 학번, 이름
class Student:
    def __init__(self, student_number, name):
        self.student_number = student_number
        self.name = name
    def __str__(self):
        return f'학번: {self.student_number}\t 이름: {self.name}'
    def __getitem__(self, key):     #객체[key] 재정의
        if key == '학번':
            return self.student_number
        elif key == '학년':
            return self.student_number[0]


# 동아리
# 속성: 동아리명, 장소, 멤버들
# 메소드: 장소 설정하자(), 멤버 추가하자(), 활동하자()
class Club:
    count = 0   # 클래스 변수: 클래스로 만들어진 객체(모두가 공유)

    @classmethod
    def get_count_club(cls):
        return f'만들어진 클래스 수: {cls.count}'
    def __init__(self, name):
        self.name = name    #동아리 이름
        self.location = None    #장소
        self.members = []   #멤버들
        Club.count += 1 #클래스 변수를 수정
    def __str__(self):
        s = ''
        for member in self.members:
            s += str(member) + '\t'
        return f'동아리명: {self.name}\t장소: {self.location}\t멤버들: {s}'
    def set_location(self, location):
        self.location = location
    def add_member(self, student):
        self.members.append(student)    # 리스트에 아이템 추가
    def set_action(self, action):
        self.action = action
    def act(self):
        print(self.action)
    def __len__(self):  #동아리 멤버 수 리턴
        return len(self.members)
    def __del__(self):  #del 객체 했을 때, 메모리에서 삭제하기 전에 실행
        print(f'{self.name}은(는) 간다.')


학생1 = Student('2212', '인소리')
print(학생1)
학생2 = Student('2204', '김태연')
print(학생2)

동아리1 = Club('축구부')
동아리1.set_location('강당')
동아리1.set_action('축구하기')
동아리1.add_member(학생1)
동아리1.add_member(학생2)
print(동아리1)
동아리1.act()

동아리2 = Club('MSG')
동아리2.set_location('코워킹 스페이스')
동아리2.set_action('코딩하기')
동아리2.add_member(학생1)
print(동아리2)
동아리2.act()

print(Club.count)   # 동아리1.count 도 가능
print(Club.get_count_club())    # 동아리2.get_count_club()

# 축구부 멤버수 출력
print(len(동아리1.members))

#특수 메소드
#__init__(self, ...)

#__str__(self) 클래스의 객체를 문자열화 한다
#(주로 객체의 속성을 알아볼 수 있도록 정보 표시)

#__len__(self)      len(객체) 재정의
print('__len__()')
print(len(동아리1))    #동아리1의 멤버 수를 출력

#__getitem__(self, key)     #객체[key] 재정의
print('__getitem__()')
print(학생1)
print(학생1['학번'])    #print(학생1.student_number)
print(학생1['학년'])

#__del__(self)  객체를 명시적으로 지울 때 호출되는 메소드
# number = 10
# print(number)
# del number
# print(number)

print('__del__()')
print(동아리1)
del 동아리1