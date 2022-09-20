# 연예인, 가수, 배우
class Celebrity:
    def __init__(self, name):
        self.name = name
        self.debut_date = None
        self.company = None

    def set_debut_date(self, debut_date):
        self.debut_date = debut_date

    def set_company(self, company):
        self.company = company

    def __str__(self):
        return f'{self.name}\t{self.debut_date}\t{self.company}'

아이유 = Celebrity('이지은')
아이유.set_debut_date('2008-09-18')
아이유.set_company('이담엔터테인먼트')
print(아이유)

class Singer(Celebrity):
    def set_song(self, song):
        self.song = song
    def __str__(self):  # 오버라이딩, 부모 함수 호출하는 법
        return f'{super().__str__()}\t대표곡: {self.song}'

마크 = Singer('이마크')
마크.set_company('SM 엔터테인먼트')
마크.set_song('Child')
print(마크)

class Actor(Celebrity):
    def __init__(self, name):   # 부모 함수와 똑같은 형태
        super().__init__(name)  # name, debut_date, company 초기화
        self.work = None
    def set_work(self, work):
        self.work = work
    def __str__(self):
        return f'{super().__str__()}\t대표작: {self.work}'

이정재 = Actor('이정재')
이정재.set_debut_date('1993-00-00')
이정재.set_work('태양은 없다')
print(이정재)

mine = [마크, 이정재]
print(mine) # 이상하게 나옴 - 하나씩 꺼내줘야 함

for m in mine:
    print(m)