'''
옆 친구와 클래스 구조 만들고
객체화 -> 상속 -> 출력

사람 - 이름, 나이, 성별
선생님 - 과목, 담임반

클래스는 웬만하면 단수, 여러 개 담으면 복수
수치가 들어오는 값이면 숫자로 세팅
나이, 생년월일 등은 숫자, 전화번호는 문자로 처리

변수, 함수, 클래스면 명확하게

이제 더이상 내 코드는 나만 보지 않는디.

'''

class Person:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.gender = None

    def set_age(self, age): #매개 변수와 함수 이름을 같게 하지 말 것
        self.age = age

    def set_gender(self, gender):
        genders = ['여자','남자']
        if gender in genders:
            self.gender = gender

    def __str__(self):
        return f'{self.name}\t{self.age}\t{self.gender}'

# people에 값넣기
고나근샘 = Person('고낙은')
고나근샘.set_age(34)
고나근샘.set_gender('남자')
print(고나근샘)

class Teacher(Person):
    def set_subject(self, subject):
        self.subject = subject

    def set_homeroom_teacher(self, homeroom_teacher):
        self.homeroom_teacher = homeroom_teacher

    def __str__(self):
        return f'{super().__str__()}\t담당과목: {self.subject}\t담임반: {self.homeroom_teacher}'


#Teacher에 값넣기
고낙은샘 = Teacher('고낙은')

고낙은샘.set_subject('체육')
고낙은샘.set_homeroom_teacher('2-2')
print(고낙은샘)