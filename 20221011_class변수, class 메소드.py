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

# 동아리
# 속성: 동아리명, 장소, 멤버들
# 메소드: 장소 설정하자(), 멤버 추가하자(), 활동하자()
class Club:
    count = 0   # 클래스 변수: 클래스로 만들어진 객체(모두가 공유)

    @classmethod
    def get_count_club(cls):
        return f'만들어진 클래스 수: {cls.count}'
    def __init__(self, name):
        self.name = name
        self.location = None
        self.members = []
        Club.count += 1
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