from drink import Drink

class Bubbletea(Drink):
    #클래스변수
    _PEARLS = ('타피오카','코코','알로에','곤약')
    def __init__(self, name, price):
        super().__init__(name, price)   #부모의 생성자 호출(시험)
        self.pearl = 0  #0: 타피오카, 1: 코코, 2: 알로에, 3: 곤약
    def __str__(self):
        return super().__str__() + f'\t펄: {Bubbletea._PEARLS[self.pearl]} 펄'
    def set_pearl(self):
        for index, pearl_label in enumerate(Bubbletea._PEARLS):
            print(f'{index + 1}. {pearl_label} 펄')
        pearl = input("펄을 선택하세요: ")
        # if pearl == '':
        #     self.pearl = 0
        # else:
        #     self.pearl = int(pearl) - 1
        self.pearl = 0 if pearl == '' else int(pearl) - 1
    def order(self):
        #부모 order() 호출
        super().order() #컵 사이즈, 당도, 얼음량을 설정하자
        #내 set_pearl() 호출
        self.set_pearl()

버블티1 = Bubbletea('타로버블티', 3700)
버블티1.order()
print(버블티1)